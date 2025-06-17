# Generated from grammar/iDevS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,220,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,1,0,
        1,0,3,0,57,8,0,1,0,4,0,60,8,0,11,0,12,0,61,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,4,7,93,8,7,11,7,12,7,94,1,7,1,7,1,
        8,1,8,1,8,1,8,5,8,103,8,8,10,8,12,8,106,9,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,4,10,118,8,10,11,10,12,10,119,1,10,1,10,
        1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,5,13,138,8,13,10,13,12,13,141,9,13,1,13,1,13,4,13,145,8,13,
        11,13,12,13,146,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,4,15,157,
        8,15,11,15,12,15,158,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        3,16,170,8,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,4,19,184,8,19,11,19,12,19,185,1,19,1,19,1,20,1,20,1,20,
        1,20,1,20,1,20,4,20,196,8,20,11,20,12,20,197,1,20,1,20,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,24,1,24,1,24,0,0,25,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,0,3,1,0,11,15,1,0,41,42,2,0,39,
        40,42,43,211,0,50,1,0,0,0,2,65,1,0,0,0,4,74,1,0,0,0,6,77,1,0,0,0,
        8,80,1,0,0,0,10,83,1,0,0,0,12,86,1,0,0,0,14,89,1,0,0,0,16,98,1,0,
        0,0,18,109,1,0,0,0,20,113,1,0,0,0,22,123,1,0,0,0,24,126,1,0,0,0,
        26,129,1,0,0,0,28,150,1,0,0,0,30,152,1,0,0,0,32,169,1,0,0,0,34,171,
        1,0,0,0,36,175,1,0,0,0,38,179,1,0,0,0,40,189,1,0,0,0,42,201,1,0,
        0,0,44,209,1,0,0,0,46,213,1,0,0,0,48,217,1,0,0,0,50,51,5,1,0,0,51,
        52,5,42,0,0,52,53,5,2,0,0,53,54,3,2,1,0,54,56,3,14,7,0,55,57,3,20,
        10,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,60,3,26,13,0,59,
        58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,
        0,63,64,5,3,0,0,64,1,1,0,0,0,65,66,5,4,0,0,66,67,5,2,0,0,67,68,3,
        4,2,0,68,69,3,6,3,0,69,70,3,8,4,0,70,71,3,10,5,0,71,72,3,12,6,0,
        72,73,5,3,0,0,73,3,1,0,0,0,74,75,5,5,0,0,75,76,5,42,0,0,76,5,1,0,
        0,0,77,78,5,6,0,0,78,79,5,42,0,0,79,7,1,0,0,0,80,81,5,7,0,0,81,82,
        5,42,0,0,82,9,1,0,0,0,83,84,5,8,0,0,84,85,5,42,0,0,85,11,1,0,0,0,
        86,87,5,9,0,0,87,88,5,42,0,0,88,13,1,0,0,0,89,90,5,10,0,0,90,92,
        5,2,0,0,91,93,3,16,8,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,
        94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,3,0,0,97,15,1,0,0,0,98,99,7,
        0,0,0,99,100,5,42,0,0,100,104,5,2,0,0,101,103,3,18,9,0,102,101,1,
        0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,107,1,
        0,0,0,106,104,1,0,0,0,107,108,5,3,0,0,108,17,1,0,0,0,109,110,5,41,
        0,0,110,111,5,16,0,0,111,112,3,48,24,0,112,19,1,0,0,0,113,114,5,
        17,0,0,114,117,5,2,0,0,115,118,3,22,11,0,116,118,3,24,12,0,117,115,
        1,0,0,0,117,116,1,0,0,0,118,119,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,121,1,0,0,0,121,122,5,3,0,0,122,21,1,0,0,0,123,124,5,
        18,0,0,124,125,5,42,0,0,125,23,1,0,0,0,126,127,5,19,0,0,127,128,
        5,42,0,0,128,25,1,0,0,0,129,130,5,20,0,0,130,131,5,42,0,0,131,132,
        5,2,0,0,132,133,5,21,0,0,133,134,5,22,0,0,134,139,3,28,14,0,135,
        136,5,23,0,0,136,138,3,28,14,0,137,135,1,0,0,0,138,141,1,0,0,0,139,
        137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,0,0,141,139,1,0,0,0,142,
        144,5,24,0,0,143,145,3,30,15,0,144,143,1,0,0,0,145,146,1,0,0,0,146,
        144,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,5,3,0,0,149,
        27,1,0,0,0,150,151,7,1,0,0,151,29,1,0,0,0,152,153,5,25,0,0,153,154,
        5,42,0,0,154,156,5,2,0,0,155,157,3,32,16,0,156,155,1,0,0,0,157,158,
        1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,160,1,0,0,0,160,161,
        5,3,0,0,161,31,1,0,0,0,162,170,3,34,17,0,163,170,3,36,18,0,164,170,
        3,38,19,0,165,170,3,40,20,0,166,170,3,42,21,0,167,170,3,44,22,0,
        168,170,3,46,23,0,169,162,1,0,0,0,169,163,1,0,0,0,169,164,1,0,0,
        0,169,165,1,0,0,0,169,166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,
        0,170,33,1,0,0,0,171,172,5,26,0,0,172,173,5,27,0,0,173,174,3,28,
        14,0,174,35,1,0,0,0,175,176,5,28,0,0,176,177,5,29,0,0,177,178,3,
        28,14,0,178,37,1,0,0,0,179,180,5,30,0,0,180,181,5,42,0,0,181,183,
        5,2,0,0,182,184,3,32,16,0,183,182,1,0,0,0,184,185,1,0,0,0,185,183,
        1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,5,3,0,0,188,39,1,
        0,0,0,189,190,5,31,0,0,190,191,5,41,0,0,191,192,5,32,0,0,192,193,
        3,28,14,0,193,195,5,2,0,0,194,196,3,32,16,0,195,194,1,0,0,0,196,
        197,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,
        200,5,3,0,0,200,41,1,0,0,0,201,202,5,33,0,0,202,203,5,34,0,0,203,
        204,5,41,0,0,204,205,5,35,0,0,205,206,5,42,0,0,206,207,5,36,0,0,
        207,208,5,41,0,0,208,43,1,0,0,0,209,210,5,37,0,0,210,211,5,34,0,
        0,211,212,5,41,0,0,212,45,1,0,0,0,213,214,5,38,0,0,214,215,5,36,
        0,0,215,216,5,41,0,0,216,47,1,0,0,0,217,218,7,2,0,0,218,49,1,0,0,
        0,12,56,61,94,104,117,119,139,146,158,169,185,197
    ]

class iDevSParser ( Parser ):

    grammarFileName = "iDevS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'IntegrationSolution'", "'{'", "'}'", 
                     "'Infrastructure'", "'Launcher'", "'SecureHardware'", 
                     "'Compartment'", "'RootOfTrust'", "'SourceCode'", "'Services'", 
                     "'API'", "'Database'", "'Queue'", "'File'", "'Custom'", 
                     "'='", "'KeysExchange'", "'ProgramPublicKey'", "'ServicePublicKey'", 
                     "'Process'", "'uses'", "'['", "','", "']'", "'Step'", 
                     "'Read'", "'from'", "'Write'", "'to'", "'If'", "'For'", 
                     "'in'", "'Transform'", "'input='", "'operation='", 
                     "'output='", "'StoreLocalData'", "'RetrieveLocalData'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_integrationSolution = 0
    RULE_infrastructure = 1
    RULE_launcher = 2
    RULE_secureHardware = 3
    RULE_compartment = 4
    RULE_rootOfTrust = 5
    RULE_sourceCode = 6
    RULE_services = 7
    RULE_service = 8
    RULE_attrPair = 9
    RULE_keysExchange = 10
    RULE_programKey = 11
    RULE_serviceKey = 12
    RULE_process = 13
    RULE_serviceRef = 14
    RULE_step = 15
    RULE_action = 16
    RULE_read = 17
    RULE_write = 18
    RULE_ifblock = 19
    RULE_forblock = 20
    RULE_transform = 21
    RULE_storeLocal = 22
    RULE_retrieveLocal = 23
    RULE_value = 24

    ruleNames =  [ "integrationSolution", "infrastructure", "launcher", 
                   "secureHardware", "compartment", "rootOfTrust", "sourceCode", 
                   "services", "service", "attrPair", "keysExchange", "programKey", 
                   "serviceKey", "process", "serviceRef", "step", "action", 
                   "read", "write", "ifblock", "forblock", "transform", 
                   "storeLocal", "retrieveLocal", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    ID=41
    STRING=42
    NUMBER=43
    WS=44
    COMMENT=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class IntegrationSolutionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def infrastructure(self):
            return self.getTypedRuleContext(iDevSParser.InfrastructureContext,0)


        def services(self):
            return self.getTypedRuleContext(iDevSParser.ServicesContext,0)


        def keysExchange(self):
            return self.getTypedRuleContext(iDevSParser.KeysExchangeContext,0)


        def process(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ProcessContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ProcessContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_integrationSolution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntegrationSolution" ):
                listener.enterIntegrationSolution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntegrationSolution" ):
                listener.exitIntegrationSolution(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegrationSolution" ):
                return visitor.visitIntegrationSolution(self)
            else:
                return visitor.visitChildren(self)




    def integrationSolution(self):

        localctx = iDevSParser.IntegrationSolutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_integrationSolution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(iDevSParser.T__0)
            self.state = 51
            self.match(iDevSParser.STRING)
            self.state = 52
            self.match(iDevSParser.T__1)
            self.state = 53
            self.infrastructure()
            self.state = 54
            self.services()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 55
                self.keysExchange()


            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.process()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==20):
                    break

            self.state = 63
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InfrastructureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def launcher(self):
            return self.getTypedRuleContext(iDevSParser.LauncherContext,0)


        def secureHardware(self):
            return self.getTypedRuleContext(iDevSParser.SecureHardwareContext,0)


        def compartment(self):
            return self.getTypedRuleContext(iDevSParser.CompartmentContext,0)


        def rootOfTrust(self):
            return self.getTypedRuleContext(iDevSParser.RootOfTrustContext,0)


        def sourceCode(self):
            return self.getTypedRuleContext(iDevSParser.SourceCodeContext,0)


        def getRuleIndex(self):
            return iDevSParser.RULE_infrastructure

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfrastructure" ):
                listener.enterInfrastructure(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfrastructure" ):
                listener.exitInfrastructure(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfrastructure" ):
                return visitor.visitInfrastructure(self)
            else:
                return visitor.visitChildren(self)




    def infrastructure(self):

        localctx = iDevSParser.InfrastructureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_infrastructure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(iDevSParser.T__3)
            self.state = 66
            self.match(iDevSParser.T__1)
            self.state = 67
            self.launcher()
            self.state = 68
            self.secureHardware()
            self.state = 69
            self.compartment()
            self.state = 70
            self.rootOfTrust()
            self.state = 71
            self.sourceCode()
            self.state = 72
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LauncherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_launcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLauncher" ):
                listener.enterLauncher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLauncher" ):
                listener.exitLauncher(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLauncher" ):
                return visitor.visitLauncher(self)
            else:
                return visitor.visitChildren(self)




    def launcher(self):

        localctx = iDevSParser.LauncherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_launcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(iDevSParser.T__4)
            self.state = 75
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecureHardwareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_secureHardware

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecureHardware" ):
                listener.enterSecureHardware(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecureHardware" ):
                listener.exitSecureHardware(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecureHardware" ):
                return visitor.visitSecureHardware(self)
            else:
                return visitor.visitChildren(self)




    def secureHardware(self):

        localctx = iDevSParser.SecureHardwareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_secureHardware)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(iDevSParser.T__5)
            self.state = 78
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompartmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_compartment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompartment" ):
                listener.enterCompartment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompartment" ):
                listener.exitCompartment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompartment" ):
                return visitor.visitCompartment(self)
            else:
                return visitor.visitChildren(self)




    def compartment(self):

        localctx = iDevSParser.CompartmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compartment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(iDevSParser.T__6)
            self.state = 81
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RootOfTrustContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_rootOfTrust

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRootOfTrust" ):
                listener.enterRootOfTrust(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRootOfTrust" ):
                listener.exitRootOfTrust(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRootOfTrust" ):
                return visitor.visitRootOfTrust(self)
            else:
                return visitor.visitChildren(self)




    def rootOfTrust(self):

        localctx = iDevSParser.RootOfTrustContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_rootOfTrust)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(iDevSParser.T__7)
            self.state = 84
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceCodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_sourceCode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceCode" ):
                listener.enterSourceCode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceCode" ):
                listener.exitSourceCode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSourceCode" ):
                return visitor.visitSourceCode(self)
            else:
                return visitor.visitChildren(self)




    def sourceCode(self):

        localctx = iDevSParser.SourceCodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_sourceCode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(iDevSParser.T__8)
            self.state = 87
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServicesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def service(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ServiceContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ServiceContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_services

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServices" ):
                listener.enterServices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServices" ):
                listener.exitServices(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServices" ):
                return visitor.visitServices(self)
            else:
                return visitor.visitChildren(self)




    def services(self):

        localctx = iDevSParser.ServicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_services)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(iDevSParser.T__9)
            self.state = 90
            self.match(iDevSParser.T__1)
            self.state = 92 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.service()
                self.state = 94 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                    break

            self.state = 96
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def attrPair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.AttrPairContext)
            else:
                return self.getTypedRuleContext(iDevSParser.AttrPairContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_service

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterService" ):
                listener.enterService(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitService" ):
                listener.exitService(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitService" ):
                return visitor.visitService(self)
            else:
                return visitor.visitChildren(self)




    def service(self):

        localctx = iDevSParser.ServiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 63488) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            self.match(iDevSParser.STRING)
            self.state = 100
            self.match(iDevSParser.T__1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 101
                self.attrPair()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrPairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(iDevSParser.ID, 0)

        def value(self):
            return self.getTypedRuleContext(iDevSParser.ValueContext,0)


        def getRuleIndex(self):
            return iDevSParser.RULE_attrPair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrPair" ):
                listener.enterAttrPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrPair" ):
                listener.exitAttrPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrPair" ):
                return visitor.visitAttrPair(self)
            else:
                return visitor.visitChildren(self)




    def attrPair(self):

        localctx = iDevSParser.AttrPairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attrPair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(iDevSParser.ID)
            self.state = 110
            self.match(iDevSParser.T__15)
            self.state = 111
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeysExchangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ProgramKeyContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ProgramKeyContext,i)


        def serviceKey(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ServiceKeyContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ServiceKeyContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_keysExchange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeysExchange" ):
                listener.enterKeysExchange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeysExchange" ):
                listener.exitKeysExchange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeysExchange" ):
                return visitor.visitKeysExchange(self)
            else:
                return visitor.visitChildren(self)




    def keysExchange(self):

        localctx = iDevSParser.KeysExchangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_keysExchange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(iDevSParser.T__16)
            self.state = 114
            self.match(iDevSParser.T__1)
            self.state = 117 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 117
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18]:
                    self.state = 115
                    self.programKey()
                    pass
                elif token in [19]:
                    self.state = 116
                    self.serviceKey()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 119 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==18 or _la==19):
                    break

            self.state = 121
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_programKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramKey" ):
                listener.enterProgramKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramKey" ):
                listener.exitProgramKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramKey" ):
                return visitor.visitProgramKey(self)
            else:
                return visitor.visitChildren(self)




    def programKey(self):

        localctx = iDevSParser.ProgramKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_programKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(iDevSParser.T__17)
            self.state = 124
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_serviceKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceKey" ):
                listener.enterServiceKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceKey" ):
                listener.exitServiceKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServiceKey" ):
                return visitor.visitServiceKey(self)
            else:
                return visitor.visitChildren(self)




    def serviceKey(self):

        localctx = iDevSParser.ServiceKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_serviceKey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(iDevSParser.T__18)
            self.state = 127
            self.match(iDevSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def serviceRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ServiceRefContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ServiceRefContext,i)


        def step(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.StepContext)
            else:
                return self.getTypedRuleContext(iDevSParser.StepContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_process

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcess" ):
                listener.enterProcess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcess" ):
                listener.exitProcess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProcess" ):
                return visitor.visitProcess(self)
            else:
                return visitor.visitChildren(self)




    def process(self):

        localctx = iDevSParser.ProcessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_process)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(iDevSParser.T__19)
            self.state = 130
            self.match(iDevSParser.STRING)
            self.state = 131
            self.match(iDevSParser.T__1)
            self.state = 132
            self.match(iDevSParser.T__20)
            self.state = 133
            self.match(iDevSParser.T__21)
            self.state = 134
            self.serviceRef()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 135
                self.match(iDevSParser.T__22)
                self.state = 136
                self.serviceRef()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(iDevSParser.T__23)
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.step()
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 148
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServiceRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def ID(self):
            return self.getToken(iDevSParser.ID, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_serviceRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServiceRef" ):
                listener.enterServiceRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServiceRef" ):
                listener.exitServiceRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServiceRef" ):
                return visitor.visitServiceRef(self)
            else:
                return visitor.visitChildren(self)




    def serviceRef(self):

        localctx = iDevSParser.ServiceRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_serviceRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ActionContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ActionContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_step

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStep" ):
                listener.enterStep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStep" ):
                listener.exitStep(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStep" ):
                return visitor.visitStep(self)
            else:
                return visitor.visitChildren(self)




    def step(self):

        localctx = iDevSParser.StepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_step)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(iDevSParser.T__24)
            self.state = 153
            self.match(iDevSParser.STRING)
            self.state = 154
            self.match(iDevSParser.T__1)
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.action()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 424463564800) != 0)):
                    break

            self.state = 160
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def read(self):
            return self.getTypedRuleContext(iDevSParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(iDevSParser.WriteContext,0)


        def ifblock(self):
            return self.getTypedRuleContext(iDevSParser.IfblockContext,0)


        def forblock(self):
            return self.getTypedRuleContext(iDevSParser.ForblockContext,0)


        def transform(self):
            return self.getTypedRuleContext(iDevSParser.TransformContext,0)


        def storeLocal(self):
            return self.getTypedRuleContext(iDevSParser.StoreLocalContext,0)


        def retrieveLocal(self):
            return self.getTypedRuleContext(iDevSParser.RetrieveLocalContext,0)


        def getRuleIndex(self):
            return iDevSParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = iDevSParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_action)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.read()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.write()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.ifblock()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.forblock()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 166
                self.transform()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 167
                self.storeLocal()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 7)
                self.state = 168
                self.retrieveLocal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def serviceRef(self):
            return self.getTypedRuleContext(iDevSParser.ServiceRefContext,0)


        def getRuleIndex(self):
            return iDevSParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = iDevSParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(iDevSParser.T__25)
            self.state = 172
            self.match(iDevSParser.T__26)
            self.state = 173
            self.serviceRef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def serviceRef(self):
            return self.getTypedRuleContext(iDevSParser.ServiceRefContext,0)


        def getRuleIndex(self):
            return iDevSParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = iDevSParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(iDevSParser.T__27)
            self.state = 176
            self.match(iDevSParser.T__28)
            self.state = 177
            self.serviceRef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ActionContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ActionContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_ifblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfblock" ):
                listener.enterIfblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfblock" ):
                listener.exitIfblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfblock" ):
                return visitor.visitIfblock(self)
            else:
                return visitor.visitChildren(self)




    def ifblock(self):

        localctx = iDevSParser.IfblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ifblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(iDevSParser.T__29)
            self.state = 180
            self.match(iDevSParser.STRING)
            self.state = 181
            self.match(iDevSParser.T__1)
            self.state = 183 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.action()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 424463564800) != 0)):
                    break

            self.state = 187
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForblockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(iDevSParser.ID, 0)

        def serviceRef(self):
            return self.getTypedRuleContext(iDevSParser.ServiceRefContext,0)


        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(iDevSParser.ActionContext)
            else:
                return self.getTypedRuleContext(iDevSParser.ActionContext,i)


        def getRuleIndex(self):
            return iDevSParser.RULE_forblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForblock" ):
                listener.enterForblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForblock" ):
                listener.exitForblock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForblock" ):
                return visitor.visitForblock(self)
            else:
                return visitor.visitChildren(self)




    def forblock(self):

        localctx = iDevSParser.ForblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(iDevSParser.T__30)
            self.state = 190
            self.match(iDevSParser.ID)
            self.state = 191
            self.match(iDevSParser.T__31)
            self.state = 192
            self.serviceRef()
            self.state = 193
            self.match(iDevSParser.T__1)
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.action()
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 424463564800) != 0)):
                    break

            self.state = 199
            self.match(iDevSParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(iDevSParser.ID)
            else:
                return self.getToken(iDevSParser.ID, i)

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_transform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransform" ):
                listener.enterTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransform" ):
                listener.exitTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransform" ):
                return visitor.visitTransform(self)
            else:
                return visitor.visitChildren(self)




    def transform(self):

        localctx = iDevSParser.TransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_transform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(iDevSParser.T__32)
            self.state = 202
            self.match(iDevSParser.T__33)
            self.state = 203
            self.match(iDevSParser.ID)
            self.state = 204
            self.match(iDevSParser.T__34)
            self.state = 205
            self.match(iDevSParser.STRING)
            self.state = 206
            self.match(iDevSParser.T__35)
            self.state = 207
            self.match(iDevSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreLocalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(iDevSParser.ID, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_storeLocal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStoreLocal" ):
                listener.enterStoreLocal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStoreLocal" ):
                listener.exitStoreLocal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStoreLocal" ):
                return visitor.visitStoreLocal(self)
            else:
                return visitor.visitChildren(self)




    def storeLocal(self):

        localctx = iDevSParser.StoreLocalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_storeLocal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(iDevSParser.T__36)
            self.state = 210
            self.match(iDevSParser.T__33)
            self.state = 211
            self.match(iDevSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetrieveLocalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(iDevSParser.ID, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_retrieveLocal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetrieveLocal" ):
                listener.enterRetrieveLocal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetrieveLocal" ):
                listener.exitRetrieveLocal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetrieveLocal" ):
                return visitor.visitRetrieveLocal(self)
            else:
                return visitor.visitChildren(self)




    def retrieveLocal(self):

        localctx = iDevSParser.RetrieveLocalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_retrieveLocal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(iDevSParser.T__37)
            self.state = 214
            self.match(iDevSParser.T__35)
            self.state = 215
            self.match(iDevSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(iDevSParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(iDevSParser.NUMBER, 0)

        def getRuleIndex(self):
            return iDevSParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = iDevSParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14843406974976) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





