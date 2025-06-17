import os
from jinja2 import Environment, FileSystemLoader
from src.visitor import ModelVisitor
from antlr4 import *
from src.iDevSLexer import iDevSLexer
from src.iDevSParser import iDevSParser


def generate_code(model):
    env = Environment(loader=FileSystemLoader('templates'))
    os.makedirs('generated', exist_ok=True)

    c_template = env.get_template('integration_process.c.j2')
    h_template = env.get_template('integration_process.h.j2')
    makefile_template = env.get_template('Makefile.j2')

    with open('generated/integration_process.c', 'w') as f:
        f.write(c_template.render(model=model))

    with open('generated/integration_process.h', 'w') as f:
        f.write(h_template.render(model=model))

    with open('generated/Makefile', 'w') as f:
        f.write(makefile_template.render(model=model))


def main():
    input_stream = FileStream('examples/purchase_pipeline.idevs', encoding='utf-8')
    lexer = iDevSLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = iDevSParser(stream)
    tree = parser.integrationSolution()

    visitor = ModelVisitor()
    model = visitor.visit(tree)

    generate_code(model)
    print("Code generated in /generated")


if __name__ == '__main__':
    main()

