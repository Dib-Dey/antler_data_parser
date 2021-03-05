lexer grammar Lexer;
////////////////////////////////////////////////////////////////////////////////
//                            Default Lexicons                                //
////////////////////////////////////////////////////////////////////////////////
fragment WS: [\t ]+;
fragment NL: WS? ('\r'* '\n')+;
fragment CHANNEL: 'C' [0-9];
fragment DIMM: 'D' [0-9];
fragment RANK: 'R' [0-9];
fragment INT: [0-9]+;
//fragment HEX: '0x' ('0'..'9' | 'a'..'f' | 'A'..'F')+;
fragment HEX: '0' [xX] [0-9a-fA-F]+;


// BIOS Information
BIOS_ID: 'BIOS ID: ' [A-Z0-9.]+;

////////////////////////////////////////////////////////////////////////////////
PCIEBAR_VALUE:'PCIEXBAR' -> mode(PCIEBAR_VALUE_MODE);
////////////////////////////////////////////////////////////////////////////////

TEXT: .+? -> skip;
mode PCIEBAR_VALUE_MODE;
PCIEBAR_VALUE_MODE_INTERMEDIATE: WS* 'is' WS* -> skip;
PCIEBAR_VALUE_MODE_FINAL_VALUE: [0-9a-fA-F]+;
PCIEBAR_VALUE_MODE_END: NL -> skip, mode(DEFAULT_MODE);