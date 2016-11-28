# -*- coding: utf-8 -*-
'''

@author: aschiweck

'''

from SolvisRemote import SolvisRemote

# new SolvisRemote instance with ip and login credentials
sr = SolvisRemote("192.168.3.40", "USERNAME", "PASSWORD")

# update and return collected data
data = sr.data()

# print all gathered data
# print str(data)

# print only key, value pairs
# print str([ key + ': '+str(data[key]['value']) for key in data.keys() ])

# print a simple debugging view
out = []
for key in sorted(data.keys()):
    title = data[key]['title']
    value = data[key]['value']
    unit = data[key]['unit'] if data[key]['unit'] else ''
    raw = data[key]['raw']
    out.append("%s [%s]: %s%s (0x%s)" % (title, key, value, unit, raw))
out.sort()
print "\n".join(out)

# gather and print last interpreted index from raw data
positions = [ pos[1]['start'] + pos[1]['size'] for pos in sr.position.items() ]
positions = sorted(positions)
indexed = positions[-1]
print '\n' + sr._raw[:indexed] + ' [<- decoded ] ' + sr._raw[indexed:]
