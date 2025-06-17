from antlr4 import *
from iDevSLexer import iDevSLexer
from iDevSParser import iDevSParser

def main():
    input_stream = FileStream('examples/purchase_pipeline.idevs', encoding='utf-8')
    lexer = iDevSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = iDevSParser(stream)
    tree = parser.integrationSolution()

    print("Parse tree:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()
