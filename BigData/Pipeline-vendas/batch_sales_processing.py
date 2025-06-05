from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, desc
from pymongo import MongoClient

# Inicializar a SparkSession
spark = SparkSession.builder \
    .appName("Batch Sales Processing") \
    .getOrCreate()

# Configuração do MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["sales_db"]  # Nome do banco de dados
total_sales_collection = db["total_sales"]  # Coleção para o total de vendas
average_sales_collection = db["average_sales"]  # Coleção para a média de vendas

# Carregar o arquivo CSV
data = spark.read.option("header", "true").csv("sales_data.csv")

# Limpar e converter dados
clean_data = data.filter(col("Produto").isNotNull())
clean_data = clean_data.withColumn("Preço Unitário (R$)", col("Preço Unitário (R$)").cast("double"))
clean_data = clean_data.withColumn("Quantidade Vendida", col("Quantidade Vendida").cast("int"))
clean_data = clean_data.withColumn("Total de Vendas (R$)", col("Total de Vendas (R$)").cast("double"))

# Calcular o total de vendas por categoria
total_sales = clean_data.groupBy("Categoria").sum("Total de Vendas (R$)")
total_sales = total_sales.withColumnRenamed("sum(Total de Vendas (R$))", "Total de Vendas por Categoria")

# Ordenar categorias por total de vendas (decrescente)
sorted_sales = total_sales.orderBy(desc("Total de Vendas por Categoria"))

# Calcular a média de vendas por categoria
average_sales = clean_data.groupBy("Categoria").agg(avg("Total de Vendas (R$)").alias("Média de Vendas por Categoria"))

# Exibir os resultados no console
print("Total de Vendas por Categoria:")
sorted_sales.show()

print("Média de Vendas por Categoria:")
average_sales.show()

# Converter os resultados para listas de dicionários e salvar no MongoDB
total_sales_dicts = [row.asDict() for row in sorted_sales.collect()]
average_sales_dicts = [row.asDict() for row in average_sales.collect()]

# Inserir os dados no MongoDB
total_sales_collection.delete_many({})  # Limpar a coleção antes de inserir
total_sales_collection.insert_many(total_sales_dicts)

average_sales_collection.delete_many({})  # Limpar a coleção antes de inserir
average_sales_collection.insert_many(average_sales_dicts)

# Salvar os resultados em um diretório CSV
sorted_sales.write.mode("overwrite").csv("output_total_sales_by_category", header=True)
average_sales.write.mode("overwrite").csv("output_average_sales_by_category", header=True)

# Finalizar a SparkSession
spark.stop()

print("Os resultados foram salvos no MongoDB!")

