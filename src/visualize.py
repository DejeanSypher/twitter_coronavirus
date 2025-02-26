#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)

to_plot = items[:10]
keys = [x[0] for x in to_plot][::-1]
values = [y[1] for y in to_plot][::-1]

plt.bar(range(len(keys)), values)
plt.ylabel('Number of Tweets')
plt.xticks(range(len(keys)), keys)

if 'lang' in args.input_path:
    plt.xlabel('Language')
    plt.savefig(f'{args.key}_(lang).png')
else:
    plt.xlabel('Country')
    plt.savefig(f'{args.key}_(country).png')

