# -*- coding: utf-8 -*-
'''

@author: aschiweck

'''
import base64
import urllib2
import random
import xml.etree.ElementTree as ET

class SolvisRemote:
    """
    """

    host = ''
    username = ''
    password = ''
    realm = 'SolvisRemote'

    _raw = ''
    _data = ''

    PROTOCOL = 'http'
    PATH = 'sc2_val.xml'

    # unused
    position = {}
    position['header'] = {'title': 'Header', 'start': 0, 'size': 12, 'unit': None}
    position['time'] = {'title': 'Uhrzeit', 'start': 12, 'size': 6, 'unit': None}
    position['typeofinstallation'] = {'title': 'Anlagentyp', 'start': 18, 'size': 4, 'unit': None}
    position['system'] = {'title': 'Systemnummer', 'start': 22, 'size': 4, 'unit': None}
    # temps
    position['s1'] = {'title': 'Warmwasserpuffer', 'start': 26, 'size': 4, 'unit': 'C'}
    position['s2'] = {'title': 'Warmwassertemperatur', 'start': 30, 'size': 4, 'unit': 'C'}
    position['s3'] = {'title': 'Speicherreferenz', 'start': 34, 'size': 4, 'unit': 'C'}
    position['s4'] = {'title': 'Heizungspuffer oben', 'start': 38, 'size': 4, 'unit': 'C'}
    position['s5'] = {'title': 'Vorlauftemperatur', 'start': 42, 'size': 4, 'unit': 'C'}
    position['s6'] = {'title': 'Rücklauftemperatur', 'start': 46, 'size': 4, 'unit': 'C'}
    position['s7'] = {'title': '<Unbekannt>', 'start': 50, 'size': 4, 'unit': None}
    position['s8'] = {'title': 'Kollektortemperatur', 'start': 54, 'size': 4, 'unit': 'C'}
    position['s9'] = {'title': 'Heizungspuffer unten', 'start': 58, 'size': 4, 'unit': 'C'}
    position['s10'] = {'title': 'Außentemperatur', 'start': 62, 'size': 4, 'unit': 'C'}
    position['s11'] = {'title': 'Zirkulationstemperatur', 'start': 66, 'size': 4, 'unit': 'C'}
    position['s12'] = {'title': 'Vorlauftemperatur', 'start': 70, 'size': 4, 'unit': 'C'}
    position['s13'] = {'title': 'Vorlauftemperatur', 'start': 74, 'size': 4, 'unit': 'C'}
    position['s14'] = {'title': '<Unbekannt>', 'start': 78, 'size': 4, 'unit': None}
    position['s15'] = {'title': '<Unbekannt>', 'start': 82, 'size': 4, 'unit': None}
    position['s16'] = {'title': '<Unbekannt>', 'start': 86, 'size': 4, 'unit': None}
    # flow
    position['s17'] = {'title': 'Durchfluss', 'start': 90, 'size': 4, 'unit': 'l/h'}
    position['s18'] = {'title': 'Durchfluss', 'start': 94, 'size': 4, 'unit': 'l/m'}
    # analogue in
    position['ai1'] = {'title': '<Unbekannt>', 'start': 98, 'size': 4, 'unit': None}
    position['ai2'] = {'title': '<Unbekannt>', 'start': 102, 'size': 4, 'unit': None}
    position['ai3'] = {'title': '<Unbekannt>', 'start': 106, 'size': 4, 'unit': None}
    # analog out
    position['ao1'] = {'title': '<Unbekannt>', 'start': 110, 'size': 2, 'unit': None}
    position['ao2'] = {'title': '<Unbekannt>', 'start': 112, 'size': 2, 'unit': None}
    position['ao3'] = {'title': '<Unbekannt>', 'start': 114, 'size': 2, 'unit': None}
    position['ao4'] = {'title': '<Unbekannt>', 'start': 116, 'size': 2, 'unit': None}
    # room sensor
    position['rf1'] = {'title': 'Raumtemperatur', 'start': 118, 'size': 4, 'unit': 'C'}
    position['rf2'] = {'title': 'Raumtemperatur', 'start': 122, 'size': 4, 'unit': 'C'}
    position['rf3'] = {'title': 'Raumtemperatur', 'start': 126, 'size': 4, 'unit': 'C'}
    # outputs
    position['a1'] = {'title': 'Solarpumpe', 'start': 130, 'size': 2, 'unit': None}
    position['a2'] = {'title': 'Warmwasserpumpe', 'start': 132, 'size': 2, 'unit': None}
    position['a3'] = {'title': 'Heizkreispumpe', 'start': 134, 'size': 2, 'unit': None}
    position['a4'] = {'title': 'Heizkreispumpe', 'start': 136, 'size': 2, 'unit': None}
    position['a5'] = {'title': 'Zirkulationspumpe', 'start': 138, 'size': 2, 'unit': None}
    position['a6'] = {'title': 'Heizkreispumpe', 'start': 140, 'size': 2, 'unit': None}
    position['a7'] = {'title': '<Unbekannt>', 'start': 142, 'size': 2, 'unit': None}
    position['a8'] = {'title': '<Unbekannt>', 'start': 144, 'size': 2, 'unit': None}
    position['a9'] = {'title': '<Unbekannt>', 'start': 146, 'size': 2, 'unit': None}
    position['a10'] = {'title': '<Unbekannt>', 'start': 148, 'size': 2, 'unit': None}
    position['a11'] = {'title': '<Unbekannt>', 'start': 150, 'size': 2, 'unit': None}
    position['a12'] = {'title': 'Nachheizung', 'start': 152, 'size': 2, 'unit': None}
    position['a13'] = {'title': '<Unbekannt>', 'start': 154, 'size': 2, 'unit': None}
    position['a14'] = {'title': '<Unbekannt>', 'start': 156, 'size': 2, 'unit': None}
    # unused
    position['unused0'] = {'title': '<Unbenutzt>', 'start': 158, 'size': 16, 'unit': None}
    # solar yield
    position['sev'] = {'title': 'Ertrag Solar', 'start': 174, 'size': 4, 'unit': 'kWh'}
    # unused
    position['unused1'] = {'title': '<Unbenutzt>', 'start': 178, 'size': 10, 'unit': None}
    # analogue out 5
    position['ao5'] = {'title': '<Unbekannt>', 'start': 188, 'size': 2, 'unit': None}
    # unused
    position['unused2'] = {'title': '<Unbenutzt>', 'start': 190, 'size': 14, 'unit': None}
    # serie7
    position['serie7'] = {'title': 'Serie 7', 'start': 204, 'size': 2, 'unit': None}
    # unused
    position['unused4'] = {'title': '<Unbenutzt>', 'start': 206, 'size': 2, 'unit': None}
    position['unused5'] = {'title': '<Unbenutzt>', 'start': 208, 'size': 2, 'unit': None}
    # solar power
    position['slv'] = {'title': 'Aktuelle Leistung', 'start': 210, 'size': 4, 'unit': 'kW'}


    def __init__(self, host, username, password, realm='SolvisRemote'):
        """
        """
        self.host = host
        self.username = username
        self.password = password
        self.realm = realm

        # digest auth init
        auth_handler = urllib2.HTTPDigestAuthHandler()
        auth_handler.add_password(self.realm, self.PROTOCOL+'://'+self.host, self.username, self.password)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)

        # data init
        self._update()


    def _url(self):
        """
        """
        dummy = random.randint(10000000, 99999999)
        return "%s://%s/%s?dummy=%s" % (self.PROTOCOL, self.host, self.PATH, dummy)


    def _update(self):
        """
        """
        self._raw = urllib2.urlopen(self._url())
        tree = ET.parse(self._raw)
        root = tree.getroot()
        self._raw = root.find("data").text
        self._data = self._decode()


    def data(self):
        """
        """
        self._update()
        return self._data


    def raw(self):
        """
        """
        self._update()
        return self._raw


    def _convert(self, hexstring, limited=False):
        """
        """
        hx = hexstring.decode('hex')
        hx = hx[::-1]
        value = int(hx.encode('hex'), 16)

        if limited and ( value > 32767 ):
            value -= 65536

        return  value


    def _decode(self):
        """
        """

        # isSerie7 = 0
        # P2=0
        # P5=0

        values = {}
        for value in self.position.keys():
            values[value] = {
                'title': self.position[value]['title'],
                'value': None,
                'unit': self.position[value]['unit'],
                'raw': self._raw[self.position[value]['start']:self.position[value]['start']+self.position[value]['size']]
            }

        # temps
        values['s1']['value'] = \
            self._convert(values['s1']['raw'], True) / 10.0
        values['s2']['value'] = \
            self._convert(values['s2']['raw'], True) / 10.0
        values['s3']['value'] = \
            self._convert(values['s3']['raw'], True) / 10.0
        values['s4']['value'] = \
            self._convert(values['s4']['raw'], True) / 10.0
        values['s5']['value'] = \
            self._convert(values['s5']['raw'], True) / 10.0
        values['s6']['value'] = \
            self._convert(values['s6']['raw'], True) / 10.0
        values['s7']['value'] = \
            self._convert(values['s7']['raw'], True) / 10.0
        values['s8']['value'] = \
            self._convert(values['s8']['raw'], True) / 10.0
        values['s9']['value'] = \
            self._convert(values['s9']['raw'], True) / 10.0
        values['s10']['value'] = \
            self._convert(values['s10']['raw'], True) / 10.0
        values['s11']['value'] = \
            self._convert(values['s11']['raw'], True) / 10.0
        values['s12']['value'] = \
            self._convert(values['s12']['raw'], True) / 10.0
        values['s13']['value'] = \
            self._convert(values['s13']['raw'], True) / 10.0
        values['s14']['value'] = \
            self._convert(values['s14']['raw'], True) / 10.0
        values['s15']['value'] = \
            self._convert(values['s15']['raw'], True) / 10.0
        values['s16']['value'] = \
            self._convert(values['s16']['raw'], True) / 10.0

        # flow
        values['s17']['value'] = \
            self._convert(values['s17']['raw']) / 10.0
        values['s18']['value'] = \
            self._convert(values['s18']['raw']) / 10.0

        # analogue in
        values['ai1']['value'] = \
            self._convert(values['ai1']['raw']) / 10.0
        values['ai2']['value'] = \
            self._convert(values['ai2']['raw']) / 10.0
        values['ai3']['value'] = \
            self._convert(values['ai3']['raw']) / 10.0

        # analogue out
        values['ao1']['value'] = \
            self._convert(values['ao1']['raw']) / 10.0
        # P2 = values['ao1']['value']
        values['ao2']['value'] = \
            self._convert(values['ao2']['raw']) / 10.0
        values['ao3']['value'] = \
            self._convert(values['ao3']['raw']) / 10.0
        values['ao4']['value'] = \
            self._convert(values['ao4']['raw']) / 10.0

        # room sensor
        values['rf1']['value'] = \
            self._convert(values['rf1']['raw'], True) / 10.0
        values['rf2']['value'] = \
            self._convert(values['rf2']['raw'], True) / 10.0
        values['rf3']['value'] = \
            self._convert(values['rf3']['raw'], True) / 10.0

        # outputs
        values['a1']['value'] = \
            'on' if self._convert(values['a1']['raw']) else 'off'

        # if isSerie7:
	#     if i == 28: value=P2
	#     elif i == 29: value=P5

        values['a2']['value'] = \
            'on' if self._convert(values['a2']['raw']) else 'off'
        values['a3']['value'] = \
            'on' if self._convert(values['a3']['raw']) else 'off'
        values['a4']['value'] = \
            'on' if self._convert(values['a4']['raw']) else 'off'
        values['a5']['value'] = \
            'on' if self._convert(values['a5']['raw']) else 'off'
        values['a6']['value'] = \
            'on' if self._convert(values['a6']['raw']) else 'off'
        values['a7']['value'] = \
            'on' if self._convert(values['a7']['raw']) else 'off'
        values['a8']['value'] = \
            'on' if self._convert(values['a8']['raw']) else 'off'
        values['a9']['value'] = \
            'on' if self._convert(values['a9']['raw']) else 'off'
        values['a10']['value'] = \
            'on' if self._convert(values['a10']['raw']) else 'off'
        values['a11']['value'] = \
            'on' if self._convert(values['a11']['raw']) else 'off'
        values['a12']['value'] = \
            'on' if self._convert(values['a12']['raw']) else 'off'
        values['a13']['value'] = \
            'on' if self._convert(values['a13']['raw']) else 'off'
        values['a14']['value'] = \
            'on' if self._convert(values['a14']['raw']) else 'off'
        values['a14']['value'] = \
            'on' if self._convert(values['a14']['raw']) else 'off'

        # solar yield
        values['sev']['value'] = \
            self._convert(values['sev']['raw'])

        # analogue out 5
        values['ao5']['value'] = \
            self._convert(values['ao5']['raw'])
        # P5 = values['ao5']['value']

        # serie7
        values['serie7']['value'] = \
            True if (self._convert(values['serie7']['raw']) >= 192) else False

        # solar power
        values['slv']['value'] = \
            self._convert(values['slv']['raw']) / 10.0

        return values
