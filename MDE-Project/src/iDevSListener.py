# Generated from grammar/iDevS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .iDevSParser import iDevSParser
else:
    from iDevSParser import iDevSParser

# This class defines a complete listener for a parse tree produced by iDevSParser.
class iDevSListener(ParseTreeListener):

    # Enter a parse tree produced by iDevSParser#integrationSolution.
    def enterIntegrationSolution(self, ctx:iDevSParser.IntegrationSolutionContext):
        pass

    # Exit a parse tree produced by iDevSParser#integrationSolution.
    def exitIntegrationSolution(self, ctx:iDevSParser.IntegrationSolutionContext):
        pass


    # Enter a parse tree produced by iDevSParser#infrastructure.
    def enterInfrastructure(self, ctx:iDevSParser.InfrastructureContext):
        pass

    # Exit a parse tree produced by iDevSParser#infrastructure.
    def exitInfrastructure(self, ctx:iDevSParser.InfrastructureContext):
        pass


    # Enter a parse tree produced by iDevSParser#launcher.
    def enterLauncher(self, ctx:iDevSParser.LauncherContext):
        pass

    # Exit a parse tree produced by iDevSParser#launcher.
    def exitLauncher(self, ctx:iDevSParser.LauncherContext):
        pass


    # Enter a parse tree produced by iDevSParser#secureHardware.
    def enterSecureHardware(self, ctx:iDevSParser.SecureHardwareContext):
        pass

    # Exit a parse tree produced by iDevSParser#secureHardware.
    def exitSecureHardware(self, ctx:iDevSParser.SecureHardwareContext):
        pass


    # Enter a parse tree produced by iDevSParser#compartment.
    def enterCompartment(self, ctx:iDevSParser.CompartmentContext):
        pass

    # Exit a parse tree produced by iDevSParser#compartment.
    def exitCompartment(self, ctx:iDevSParser.CompartmentContext):
        pass


    # Enter a parse tree produced by iDevSParser#rootOfTrust.
    def enterRootOfTrust(self, ctx:iDevSParser.RootOfTrustContext):
        pass

    # Exit a parse tree produced by iDevSParser#rootOfTrust.
    def exitRootOfTrust(self, ctx:iDevSParser.RootOfTrustContext):
        pass


    # Enter a parse tree produced by iDevSParser#sourceCode.
    def enterSourceCode(self, ctx:iDevSParser.SourceCodeContext):
        pass

    # Exit a parse tree produced by iDevSParser#sourceCode.
    def exitSourceCode(self, ctx:iDevSParser.SourceCodeContext):
        pass


    # Enter a parse tree produced by iDevSParser#services.
    def enterServices(self, ctx:iDevSParser.ServicesContext):
        pass

    # Exit a parse tree produced by iDevSParser#services.
    def exitServices(self, ctx:iDevSParser.ServicesContext):
        pass


    # Enter a parse tree produced by iDevSParser#service.
    def enterService(self, ctx:iDevSParser.ServiceContext):
        pass

    # Exit a parse tree produced by iDevSParser#service.
    def exitService(self, ctx:iDevSParser.ServiceContext):
        pass


    # Enter a parse tree produced by iDevSParser#attrPair.
    def enterAttrPair(self, ctx:iDevSParser.AttrPairContext):
        pass

    # Exit a parse tree produced by iDevSParser#attrPair.
    def exitAttrPair(self, ctx:iDevSParser.AttrPairContext):
        pass


    # Enter a parse tree produced by iDevSParser#keysExchange.
    def enterKeysExchange(self, ctx:iDevSParser.KeysExchangeContext):
        pass

    # Exit a parse tree produced by iDevSParser#keysExchange.
    def exitKeysExchange(self, ctx:iDevSParser.KeysExchangeContext):
        pass


    # Enter a parse tree produced by iDevSParser#programKey.
    def enterProgramKey(self, ctx:iDevSParser.ProgramKeyContext):
        pass

    # Exit a parse tree produced by iDevSParser#programKey.
    def exitProgramKey(self, ctx:iDevSParser.ProgramKeyContext):
        pass


    # Enter a parse tree produced by iDevSParser#serviceKey.
    def enterServiceKey(self, ctx:iDevSParser.ServiceKeyContext):
        pass

    # Exit a parse tree produced by iDevSParser#serviceKey.
    def exitServiceKey(self, ctx:iDevSParser.ServiceKeyContext):
        pass


    # Enter a parse tree produced by iDevSParser#process.
    def enterProcess(self, ctx:iDevSParser.ProcessContext):
        pass

    # Exit a parse tree produced by iDevSParser#process.
    def exitProcess(self, ctx:iDevSParser.ProcessContext):
        pass


    # Enter a parse tree produced by iDevSParser#serviceRef.
    def enterServiceRef(self, ctx:iDevSParser.ServiceRefContext):
        pass

    # Exit a parse tree produced by iDevSParser#serviceRef.
    def exitServiceRef(self, ctx:iDevSParser.ServiceRefContext):
        pass


    # Enter a parse tree produced by iDevSParser#step.
    def enterStep(self, ctx:iDevSParser.StepContext):
        pass

    # Exit a parse tree produced by iDevSParser#step.
    def exitStep(self, ctx:iDevSParser.StepContext):
        pass


    # Enter a parse tree produced by iDevSParser#action.
    def enterAction(self, ctx:iDevSParser.ActionContext):
        pass

    # Exit a parse tree produced by iDevSParser#action.
    def exitAction(self, ctx:iDevSParser.ActionContext):
        pass


    # Enter a parse tree produced by iDevSParser#read.
    def enterRead(self, ctx:iDevSParser.ReadContext):
        pass

    # Exit a parse tree produced by iDevSParser#read.
    def exitRead(self, ctx:iDevSParser.ReadContext):
        pass


    # Enter a parse tree produced by iDevSParser#write.
    def enterWrite(self, ctx:iDevSParser.WriteContext):
        pass

    # Exit a parse tree produced by iDevSParser#write.
    def exitWrite(self, ctx:iDevSParser.WriteContext):
        pass


    # Enter a parse tree produced by iDevSParser#ifblock.
    def enterIfblock(self, ctx:iDevSParser.IfblockContext):
        pass

    # Exit a parse tree produced by iDevSParser#ifblock.
    def exitIfblock(self, ctx:iDevSParser.IfblockContext):
        pass


    # Enter a parse tree produced by iDevSParser#forblock.
    def enterForblock(self, ctx:iDevSParser.ForblockContext):
        pass

    # Exit a parse tree produced by iDevSParser#forblock.
    def exitForblock(self, ctx:iDevSParser.ForblockContext):
        pass


    # Enter a parse tree produced by iDevSParser#transform.
    def enterTransform(self, ctx:iDevSParser.TransformContext):
        pass

    # Exit a parse tree produced by iDevSParser#transform.
    def exitTransform(self, ctx:iDevSParser.TransformContext):
        pass


    # Enter a parse tree produced by iDevSParser#storeLocal.
    def enterStoreLocal(self, ctx:iDevSParser.StoreLocalContext):
        pass

    # Exit a parse tree produced by iDevSParser#storeLocal.
    def exitStoreLocal(self, ctx:iDevSParser.StoreLocalContext):
        pass


    # Enter a parse tree produced by iDevSParser#retrieveLocal.
    def enterRetrieveLocal(self, ctx:iDevSParser.RetrieveLocalContext):
        pass

    # Exit a parse tree produced by iDevSParser#retrieveLocal.
    def exitRetrieveLocal(self, ctx:iDevSParser.RetrieveLocalContext):
        pass


    # Enter a parse tree produced by iDevSParser#value.
    def enterValue(self, ctx:iDevSParser.ValueContext):
        pass

    # Exit a parse tree produced by iDevSParser#value.
    def exitValue(self, ctx:iDevSParser.ValueContext):
        pass



del iDevSParser