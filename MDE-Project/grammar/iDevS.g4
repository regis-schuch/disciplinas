grammar iDevS;

// ==========================================================
// Raiz
// ==========================================================

integrationSolution
    : 'IntegrationSolution' STRING '{'
        infrastructure
        services
        keysExchange?
        process+
      '}'
    ;

// ==========================================================
// Infraestrutura
// ==========================================================

infrastructure
    : 'Infrastructure' '{'
        launcher
        secureHardware
        compartment
        rootOfTrust
        sourceCode
      '}'
    ;

launcher        : 'Launcher' STRING;
secureHardware  : 'SecureHardware' STRING;
compartment     : 'Compartment' STRING;
rootOfTrust     : 'RootOfTrust' STRING;
sourceCode      : 'SourceCode' STRING;

// ==========================================================
// Serviços
// ==========================================================

services
    : 'Services' '{' service+ '}'
    ;

service
    : ('API' | 'Database' | 'Queue' | 'File' | 'Custom') STRING '{' attrPair* '}'
    ;

attrPair
    : ID '=' value
    ;

// ==========================================================
// Chaves
// ==========================================================

keysExchange
    : 'KeysExchange' '{' (programKey | serviceKey)+ '}'
    ;

programKey
    : 'ProgramPublicKey' STRING
    ;

serviceKey
    : 'ServicePublicKey' STRING
    ;

// ==========================================================
// Processo
// ==========================================================

process
    : 'Process' STRING '{'
        'uses' '[' serviceRef (',' serviceRef)* ']'
        step+
      '}'
    ;

serviceRef
    : STRING | ID
    ;

step
    : 'Step' STRING '{' action+ '}'
    ;

// ==========================================================
// Ações
// ==========================================================

action
    : read
    | write
    | ifblock
    | forblock
    | transform
    | storeLocal
    | retrieveLocal
    ;

read
    : 'Read' 'from' serviceRef
    ;

write
    : 'Write' 'to' serviceRef
    ;

ifblock
    : 'If' STRING '{' action+ '}'
    ;

forblock
    : 'For' ID 'in' serviceRef '{' action+ '}'
    ;

transform
    : 'Transform' 'input=' ID 'operation=' STRING 'output=' ID
    ;

storeLocal
    : 'StoreLocalData' 'input=' ID
    ;

retrieveLocal
    : 'RetrieveLocalData' 'output=' ID
    ;

// ==========================================================
// Regra value no parser (não no lexer)
// ==========================================================

value
    : STRING
    | NUMBER
    | 'true'
    | 'false'
    ;

// ==========================================================
// Tokens — Lexer
// ==========================================================

ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

STRING
    : '"' ( ESC | ~["\\\r\n] )* '"'
    ;

fragment ESC
    : '\\' (["\\/bfnrt] | 'u' HEX HEX HEX HEX)
    ;

fragment HEX
    : [0-9a-fA-F]
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;

