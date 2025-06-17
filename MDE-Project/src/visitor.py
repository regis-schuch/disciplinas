from src.iDevSVisitor import iDevSVisitor
from src.iDevSParser import iDevSParser
from src.idevs_model import *

class ModelVisitor(iDevSVisitor):

    def visitIntegrationSolution(self, ctx):
        name = ctx.STRING().getText().strip('"')
        infra = self.visit(ctx.infrastructure())
        services = self.visit(ctx.services())
        keys = self.visit(ctx.keysExchange()) if ctx.keysExchange() else None
        processes = [self.visit(p) for p in ctx.process()]
        return IntegrationSolution(name, infra, services, keys, processes)

    def visitInfrastructure(self, ctx):
        return Infrastructure(
            ctx.launcher().STRING().getText().strip('"'),
            ctx.secureHardware().STRING().getText().strip('"'),
            ctx.compartment().STRING().getText().strip('"'),
            ctx.rootOfTrust().STRING().getText().strip('"'),
            ctx.sourceCode().STRING().getText().strip('"')
        )

    def visitServices(self, ctx):
        return [self.visit(s) for s in ctx.service()]

    def visitService(self, ctx):
        type_ = ctx.getChild(0).getText()
        name = ctx.STRING().getText().strip('"')
        attributes = {}
        for attr in ctx.attrPair():
            key = attr.ID().getText()
            value = self.visit(attr.value())
            attributes[key] = value
        return Service(type_, name, attributes)

    def visitKeysExchange(self, ctx):
        programKeys = [k.STRING().getText().strip('"') for k in ctx.programKey()]
        serviceKeys = [k.STRING().getText().strip('"') for k in ctx.serviceKey()]
        return KeysExchange(programKeys, serviceKeys)

    def visitProcess(self, ctx):
        name = ctx.STRING().getText().strip('"')
        uses = [s.getText().strip('"') for s in ctx.serviceRef()]
        steps = [self.visit(s) for s in ctx.step()]
        return Process(name, uses, steps)

    def visitStep(self, ctx):
        name = ctx.STRING().getText().strip('"')
        actions = [self.visit(a) for a in ctx.action()]
        return Step(name, actions)

    # Actions
    def visitRead(self, ctx):
        return Action('Read', service=ctx.serviceRef().getText().strip('"'))

    def visitWrite(self, ctx):
        return Action('Write', service=ctx.serviceRef().getText().strip('"'))

    def visitIfblock(self, ctx):
        condition = ctx.STRING().getText().strip('"')
        actions = [self.visit(a) for a in ctx.action()]
        return Action('If', condition=condition, actions=actions)

    def visitForblock(self, ctx):
        var = ctx.ID().getText()
        iterable = ctx.serviceRef().getText().strip('"')
        actions = [self.visit(a) for a in ctx.action()]
        return Action('For', variable=var, iterable=iterable, actions=actions)

    def visitTransform(self, ctx):
        return Action('Transform',
                      input=ctx.ID(0).getText(),
                      operation=ctx.STRING().getText().strip('"'),
                      output=ctx.ID(1).getText())

    def visitStoreLocal(self, ctx):
        return Action('StoreLocal', input=ctx.ID().getText())

    def visitRetrieveLocal(self, ctx):
        return Action('RetrieveLocal', output=ctx.ID().getText())

    # Value
    def visitValue(self, ctx):
        if ctx.STRING():
            return ctx.STRING().getText().strip('"')
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        if ctx.getText() in ['true', 'false']:
            return ctx.getText() == 'true'
        return ctx.getText()
