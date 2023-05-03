#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

import os
import glob
import json
from collections import Counter,defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime

total = defaultdict(lambda: defaultdict(list))
file_path = glob.glob('outputs/geoTwitter*.lang')

for path in file_path:
    with open(path) as f:
        temp = json.load(f)
        filename = os.path.basename(path)
        date = filename[10:18]
        for key in args.keys:
            if key in temp:
                total[key][date].append(sum(temp[key].values()))

fig, ax = plt.subplots()
for key in args.keys:
    dates = sorted(total[key].keys())
    values = [sum(total[key][date]) for date in dates]
    days = [datetime.strptime(date, '%y-%m-%d') for date in dates]
    ax.plot(days, values, label=key)

ax.set_xlabel('Time of Year')
ax.set_ylabel('Number of Tweets')
ax.legend()

tags = [key[1:] for key in args.keys]
plt.savefig('_'.join(tags) + '.png')
