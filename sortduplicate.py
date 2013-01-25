# -*- coding: utf-8  -*-
from collections import Counter

ARRAY = [4, 3, 6, 1, 6, 2, 2, 1, 7, 6, 5, 1, 4, 7, 8, 9, 12] * 100000

def main():
    counter = Counter(ARRAY)
    t = filter(lambda x: x[1] > 1, counter.most_common())
    print [x[0] for x in t]

if __name__ == '__main__':
    main()