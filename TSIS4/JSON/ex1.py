import json

takeData = open('D:\wamp64\www\PP2\TSIS4\JSON\sample-data.json')

data = json.load(takeData)
pretty_data = json.dumps(data, indent = 4)

print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')

for i in data['imdata']:
    l1PhysIf = i['l1PhysIf']
    attributes = l1PhysIf['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(dn +'         ' + description + '                     ' + speed + '   ' + mtu)
    
takeData.close()