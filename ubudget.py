from terminaltables import SingleTable as tab
import os
import sys
import time

class col:
    r = '\033[1;31m'
    g = '\033[1;32m'
    w = '\033[1;37m'
    x = '\033[0m'

os.system('clear')

def twrite(tspace):
    for char in tspace:
        time.sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()

twrite(col.g + 'Loading data')
time.sleep(0.3)
twrite('.')
time.sleep(0.5)
twrite('.')
time.sleep(0.5)
twrite('.\n\n' + col.x)
time.sleep(0.3)

a = 550.63
asp = int(a * .15)
aem = int(a * .05)
asa = round(a - asp - aem, 2)

b = 308.20
bsp = int(b * .15)
bem = int(b * .05)
bsa = round(b - bsp - bem, 2)

x = a + b
xsp = asp + bsp
xem = aem + bem
xsa = round(asa + bsa, 2)

data = [
    ['', col.w + 'All (100%)' + col.x,
    col.w + 'Saving (80%)' + col.x,
    col.w + 'Spending (15%)' + col.x,
    col.w + 'Emergency (5%)' + col.x],

    [col.w + 'Check 1' + col.x,
    '$ %.2f' % a, '$ %.2f' % asa, '$ %.2f' % asp, '$ %.2f' % aem],
    [col.w + 'Check 2' + col.x,
    '$ %.2f' % b, '$ %.2f' % bsa, '$ %.2f' % bsp, '$ %.2f' % bem],

    [col.g + 'Total' + col.x,
    col.g + '$ %.2f' % x + col.x,
    col.g + '$ %.2f' % xsa + col.x,
    col.g + '$ %.2f' % xsp + col.x,
    col.g + '$ %.2f' % xem + col.x]
]
table = tab(data)
print(table.table + '\n')