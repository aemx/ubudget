import datetime as dt
import json
from terminaltables import SingleTable as tb

class c: r, g, w, x = '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[0m'
j = json.load(open('data.json'))
xt, yt, zt = j["p"][:]
bn, bd, bt, ba = j['t'][0]['n'], j['t'][0]['d'], j['t'][0]['t'], j['t'][0]['a']
n, d, s, x = len(ba), [], [], 0
ss, xs, ys, zs = [0] * 4

t = ['', c.w + 'All (100%)' + c.x, c.w + 'Saving (' + str(xt) + '%)' + c.x,
    c.w + 'Spending (' + str(yt) + '%)' + c.x,
    c.w + 'Emergency (' + str(zt) + '%)' + c.x]

for x in range(n):
    r = bd[x] + ' ' + c.w + bn[x] + c.x
    if bt[x] is 'D':
        xa, ya = ba[x] * (xt / 100), ba[x] * (yt / 100)
        za = ba[x] - xa - ya
        d.append([r, ba[x], xa, ya, za])
    else: d.append([r, -ba[x], 0, -ba[x], 0])
    ss += d[x][1]
    xs += d[x][2]
    ys += d[x][3]
    zs += d[x][4]
    if x is n - 1: s.extend([ss, xs, ys, zs])
    for v, w in enumerate(d[x]):
        if isinstance(w, float):
            d[x][v] = '$ {0:.2f}'.format(abs(w))
            if w > 0: d[x][v] = c.g + d[x][v] + c.x
            if w < 0: d[x][v] = c.r + d[x][v] + c.x 
        if w is 0: d[x][v] = ''
    for v, w in enumerate(s):
        if isinstance(w, float): s[v] = c.w + '$ {0:.2f}'.format(w) + c.x
    x += 1

z = [dt.datetime.now().strftime('%Y-%m-%d') + ' ' + c.w + 'GRANDTOTAL' + c.x]
z.extend(s)
print(tb([t] + d + [z]).table)