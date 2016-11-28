# SolvisRemote
A simple python wrapper to access data from a SolvisRemote.

```[~]# watch -n 2 python example.py

Every 2,0s: python example.py                                                         Mon Nov 28 18:47:58 2016

<Unbekannt> [a10]: off (0x00)
<Unbekannt> [a11]: off (0x00)
<Unbekannt> [a13]: off (0x00)
<Unbekannt> [a14]: off (0x00)
<Unbekannt> [a7]: off (0x00)
<Unbekannt> [a8]: off (0x00)
<Unbekannt> [a9]: off (0x00)
<Unbekannt> [ai1]: 0.0 (0x0000)
<Unbekannt> [ai2]: 0.0 (0x0000)
<Unbekannt> [ai3]: 0.0 (0x0000)
<Unbekannt> [ao1]: 6.3 (0x3F)
<Unbekannt> [ao2]: 7.6 (0x4C)
<Unbekannt> [ao3]: 7.6 (0x4C)
<Unbekannt> [ao4]: 1.3 (0x0D)
<Unbekannt> [ao5]: 0 (0x00)
<Unbekannt> [s14]: 250.0 (0xC409)
<Unbekannt> [s15]: 17.7 (0xB100)
<Unbekannt> [s16]: 250.0 (0xC409)
<Unbekannt> [s7]: 250.0 (0xC409)
<Unbenutzt> [unused0]: None (0x7B6D649600004419)
<Unbenutzt> [unused1]: None (0x0101010301)
<Unbenutzt> [unused2]: None (0x00000201014100)
<Unbenutzt> [unused4]: None (0x74)
<Unbenutzt> [unused5]: None (0x00)
Aktuelle Leistung [slv]: 0.0kW (0x0000)
Anlagentyp [typeofinstallation]: None (0x1200)
Außentemperatur [s10]: -2.3C (0xE9FF)
Durchfluss [s17]: 0.0l/h (0x0000)
Durchfluss [s18]: 0.0l/m (0x0000)
Ertrag Solar [sev]: 18523kWh (0x5B48)
Header [header]: None (0xAA5555AA0505)
Heizkreispumpe [a3]: on (0x64)
Heizkreispumpe [a4]: off (0x00)
Heizkreispumpe [a6]: off (0x00)
Heizungspuffer oben [s4]: 53.4C (0x1602)
Heizungspuffer unten [s9]: 39.1C (0x8701)
Kollektortemperatur [s8]: -1.6C (0xF0FF)
Nachheizung [a12]: on (0x64)
Raumtemperatur [rf1]: 22.0C (0xDC00)
Raumtemperatur [rf2]: 0.0C (0x0000)
Raumtemperatur [rf3]: 0.0C (0x0000)
Rücklauftemperatur [s6]: 14.7C (0x9300)
Serie 7 [serie7]: False (0x96)
Solarpumpe [a1]: off (0x00)
Speicherreferenz [s3]: 29.2C (0x2401)
Systemnummer [system]: None (0x0300)
Uhrzeit [time]: None (0x123330)
Vorlauftemperatur [s12]: 45.5C (0xC701)
Vorlauftemperatur [s13]: 250.0C (0xC409)
Vorlauftemperatur [s5]: 15.8C (0x9E00)
Warmwasserpuffer [s1]: 64.2C (0x8202)
Warmwasserpumpe [a2]: off (0x00)
Warmwassertemperatur [s2]: 44.9C (0xC101)
Zirkulationspumpe [a5]: off (0x00)
Zirkulationstemperatur [s11]: 35.2C (0x6001)

AA5555AA0505123330120003008202C101240116029E009300C409F0FF8701E9FF6001C701C409C409B100C40900000000000000000000
3F4C4C0DDC000000000000006400000000000000006400007B6D6496000044195B48010101030100000002010141009674000000 [<- d
ecoded ] 100B1C64A10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000

```

![data mapping 0](https://github.com/aschiweck/SolvisRemote/doc/schema.png "data mapping 0")
![data mapping 1](https://github.com/aschiweck/SolvisRemote/doc/schemam.png "data mapping 1")
