import datetime as dt
import json
from terminaltables import SingleTable as tb

j = json.load(open('data.json'))
xt, yt, zt = j["p"][:]
bn, bd = j['t'][0]['n'], j['t'][0]['d']
bt, ba = j['t'][0]['t'], j['t'][0]['a']
n, d, s, x = len(ba), [], [], 0
ss, xs, ys, zs = [0] * 4

def f(n): return float('{0:.2f}'.format(n))

t = ['', 'All (100%)',
    'Saving (' + str(xt) + '%)',
    'Spending (' + str(yt) + '%)',
    'Emergency (' + str(zt) + '%)']

for x in range(n):
    r = bd[x] + ' ' + bn[x]
    if bt[x] is 'D':
        xa = f(ba[x] * (xt / 100))
        ya = f(ba[x] * (yt / 100))
        za = f(ba[x] - xa - ya)
        d.append([r, ba[x], xa, ya, za])
    else:
        d.append([r, -ba[x], 0, -ba[x], 0])
    ss += d[x][1]
    xs += d[x][2]
    ys += d[x][3]
    zs += d[x][4]
    if x is n - 1:
        s.extend([f(ss), f(xs), f(ys), f(zs)])
    x += 1

nw = dt.datetime.now()
z = [nw.strftime('%Y-%m-%d') + ' ' + 'GRANDTOTAL']
z.extend(s)
tb = tb([t] + d + [z])
print(tb.table)