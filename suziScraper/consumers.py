from suziScraper.tasks import get_rate
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('pairs', type=str, nargs='+')
args = parser.parse_args()

results = [get_rate.delay(pair) for pair in args.pairs]
for result in results:
    pair, rate = result.get()
    print(pair, rate)
