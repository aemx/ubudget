import datetime
import json
import os
import sys
from terminaltables import SingleTable as tab
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

json = json.load(open('data.json'))

# Array of titles       ----------------------------------------------------------------------------------------------------------------
savings = json["percents"][0]
spendings = json["percents"][1]
emergency = json["percents"][2]

titles = [
    '',
    'All (100%)',
    'Saving (' + str(savings) + '%)',
    'Spending (' + str(spendings) + '%)',
    'Emergency (' + str(emergency) + '%)'
    ]

# Array of raw data [d] ----------------------------------------------------------------------------------------------------------------
base_name = json["transactions"][0]["name"]
base_date = json["transactions"][0]["date"]
base_amnt = json["transactions"][0]["amnt"]
how_many_amounts = len(base_amnt)
data = []
x = 0

for x in range(how_many_amounts):
    row_name = base_date[x] + ' ' + base_name[x]
    savings_amnt = float('{0:.2f}'.format(base_amnt[x] * (savings / 100)))
    spendings_amnt = float('{0:.2f}'.format(base_amnt[x] * (spendings / 100)))
    emergency_amnt = float('{0:.2f}'.format(base_amnt[x] - savings_amnt - spendings_amnt))
    data.append([
        row_name,
        base_amnt[x],
        savings_amnt,
        spendings_amnt,
        emergency_amnt
    ])
    x += 1

# Array of total       ----------------------------------------------------------------------------------------------------------------
sum_of_all = []
everything_all = 0
savings_all = 0
spendings_all = 0
emergency_all = 0

for x in range(how_many_amounts):
    everything_all += data[x][1]
    savings_all += data[x][2]
    spendings_all += data[x][3]
    emergency_all += data[x][4]
    if x is how_many_amounts - 1:
        sum_of_all.extend([
            float('{0:.2f}'.format(everything_all)),
            float('{0:.2f}'.format(savings_all)),
            float('{0:.2f}'.format(spendings_all)),
            float('{0:.2f}'.format(emergency_all))
        ])
    x += 1

now = datetime.datetime.now()
total = [now.strftime('%Y-%m-%d') + ' ' + 'GRANDTOTAL']
total.extend(sum_of_all)

#   ----------------------------------------------------------------------------------------------------------------------------------
table = tab([titles] + data + [total])
print(table.table + '\n')