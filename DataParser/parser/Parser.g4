parser grammar Parser;

seriallog: (pciexbar)*
          EOF;

pciexbar:PCIEBAR_VALUE PCIEBAR_VALUE_MODE_FINAL_VALUE;
biosid: BIOS_ID;