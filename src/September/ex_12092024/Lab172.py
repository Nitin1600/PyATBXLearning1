# OrderedDict
# Dictionary that remembers insertion order'
from collections import OrderedDict, defaultdict

d = dict()
d['name'] = 'Akash'
d['age'] = 25
d['id'] = 1
d['address'] = 'KA'
print(d)

od = OrderedDict()
od['banana'] = 2
od['apple'] = 1
od['pear'] = 3
print(od)

dd = defaultdict(int)
print(dd)