# Generated from grammar/iDevS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .iDevSParser import iDevSParser
else:
    from iDevSParser import iDevSParser

# This class defines a complete generic visitor for a parse tree produced by iDevSParser.

class iDevSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by iDevSParser#integrationSolution.
    def visitIntegrationSolution(self, ctx:iDevSParser.IntegrationSolutionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#infrastructure.
    def visitInfrastructure(self, ctx:iDevSParser.InfrastructureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#launcher.
    def visitLauncher(self, ctx:iDevSParser.LauncherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#secureHardware.
    def visitSecureHardware(self, ctx:iDevSParser.SecureHardwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#compartment.
    def visitCompartment(self, ctx:iDevSParser.CompartmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#rootOfTrust.
    def visitRootOfTrust(self, ctx:iDevSParser.RootOfTrustContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#sourceCode.
    def visitSourceCode(self, ctx:iDevSParser.SourceCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#services.
    def visitServices(self, ctx:iDevSParser.ServicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#service.
    def visitService(self, ctx:iDevSParser.ServiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#attrPair.
    def visitAttrPair(self, ctx:iDevSParser.AttrPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#keysExchange.
    def visitKeysExchange(self, ctx:iDevSParser.KeysExchangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#programKey.
    def visitProgramKey(self, ctx:iDevSParser.ProgramKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#serviceKey.
    def visitServiceKey(self, ctx:iDevSParser.ServiceKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#process.
    def visitProcess(self, ctx:iDevSParser.ProcessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#serviceRef.
    def visitServiceRef(self, ctx:iDevSParser.ServiceRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#step.
    def visitStep(self, ctx:iDevSParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#action.
    def visitAction(self, ctx:iDevSParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#read.
    def visitRead(self, ctx:iDevSParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#write.
    def visitWrite(self, ctx:iDevSParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#ifblock.
    def visitIfblock(self, ctx:iDevSParser.IfblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#forblock.
    def visitForblock(self, ctx:iDevSParser.ForblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#transform.
    def visitTransform(self, ctx:iDevSParser.TransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#storeLocal.
    def visitStoreLocal(self, ctx:iDevSParser.StoreLocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#retrieveLocal.
    def visitRetrieveLocal(self, ctx:iDevSParser.RetrieveLocalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by iDevSParser#value.
    def visitValue(self, ctx:iDevSParser.ValueContext):
        return self.visitChildren(ctx)



del iDevSParser