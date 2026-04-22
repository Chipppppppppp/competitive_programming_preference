def main():
    import sys, operator, math
    if sys.implementation.name == 'pypy':
        __import__("pypyjit").set_param('max_unroll_recursion=1')
    from math import gcd, floor, ceil, sqrt, isclose, pi, sin, cos, tan, asin, acos, atan, atan2, hypot, degrees, radians, log, log2, log10
    from array import array
    from collections import deque, Counter as counter, defaultdict as ddict
    from bisect import bisect_left, bisect_right
    from heapq import heappush, heappop, heapify, heappushpop, heapreplace as heappoppush, nlargest, nsmallest
    from functools import lru_cache, reduce
    from itertools import count, cycle, accumulate, chain, groupby, islice, product, permutations, combinations, combinations_with_replacement
    inf = 3074457345618258602
    mod = 998244353
    sys.setrecursionlimit(2147483647)
    readline = sys.stdin.buffer.readline
    cache = lru_cache(None)
    def input(): return readline().rstrip().decode()
    def S(): return readline().rstrip().decode()
    def Ss(): return readline().rstrip().decode().split(' ')
    def I(): return int(readline())
    def I1(): return int(readline()) - 1
    def Is(): return [int(i) for i in readline().rstrip().split(b' ') if i]
    def I1s(): return [int(i) - 1 for i in readline().rstrip().split(b' ') if i]
    def F(): return float(readline())
    def Fs(): return [float(i) for i in readline().rstrip().split(b' ') if i]
    def F1s(): return [float(i) - 1 for i in readline().rstrip().split(b' ') if i]
    
main()
