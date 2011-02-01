"""
select.py V.1.1, May 18 2007

Functions:
  select(pos, seq): find the nth rank ordered element, modifies seq in place.
  median(alist): median of a sortable list, modifying it in place.
"""

def select(pos, seq):
    """select(pos, seq): find the nth rank ordered element (the least value has rank 0).
    Note1: it modifies the seq.
    Note2: this function is useful with Psyco, otherwise .sort is faster until len(seq)>~3e6"""
    # Version 1.1, Nov 13 2004, from "Numerical Recipes".
    lo = 0
    up = len(seq) - 1
    if pos < lo or pos > up:
        raise 'Selection out of bounds.'
    else:
        while up >= pos and pos >= lo:
            i = lo
            j = up
            tempr = seq[pos]
            seq[pos] = seq[lo]
            seq[lo] = tempr
            # Split file in two
            while i < j:
                while seq[j] > tempr:
                    j -= 1
                seq[i] = seq[j]
                while i < j and seq[i] <= tempr:
                    i += 1
                seq[j] = seq[i]
            seq[i] = tempr
            # Select subfile
            if pos < i:
                up = i - 1
            else:
                lo = i + 1
        return seq[pos]


from random import choice

def median(alist):
    """median(alist): return the median of a sortable list, that is middle
    value when the values are sorted, computed with a linear algorithm.
    Note: it modifies the given list.
    If there are an odd number of elements, try to average the middle two.
    If they can't be averaged (e.g. they are strings), choose one at random.

    >>> median()
    Traceback (most recent call last):
      ...
    TypeError: median() takes exactly 1 argument (0 given)
    >>> median([])
    Traceback (most recent call last):
      ...
    TypeError: median() expected one or more values.
    >>> median([23])
    23
    >>> median(["a"])
    'a'
    >>> median([1, 2])
    1.5

    >>> freqs = {"a":0, "b":0}
    >>> for _ in xrange(1000): freqs[median(["a", "b"])] += 1
    >>> (freqs["a"] - freqs["b"]) < 100
    True

    >>> median([1, 3, 2])
    2
    >>> median(list("acb"))
    'b'
    >>> median([10, 100, 11])
    11
    >>> median([1, 4, 3, 2])
    2.5

    >>> from random import shuffle
    >>> data = range(1000)
    >>> shuffle(data)
    >>> median(data)
    499.5
    """
    alist_len = len(alist)
    if alist_len == 0:
        raise TypeError("median() expected one or more values.")
    if alist_len == 1:
        return alist[0]

    odd_items = alist_len & 1
    median_rank = alist_len // 2

    if psyco_available and alist_len > 50:
        item1 = select(median_rank, alist)
        if not odd_items:
            item2 = select(median_rank-1, alist)
    else:
        alist.sort()
        item1 = alist[median_rank]
        if not odd_items:
            item2 = alist[median_rank-1]

    if odd_items:
        return item1
    else:
        try:
            return (item1 + item2) / 2.0
        except TypeError:
            return choice([item1, item2])


try: # Import Psyco if available. It's almost necessary, otherwise .sort is faster until len(seq)>~3e6
    import psyco
except ImportError:
    psyco_available = False
else:
    psyco.bind(select)
    psyco_available = True


if __name__ == '__main__': # Some tests
    import doctest
    from random import random
    from time import clock

    doctest.testmod()
    print "Doctests finished.\n"

    raise SystemExit # ************************************************************************

    def _sort_select(pos, seq):
        return sorted(seq)[pos]

    for n in (10, 100, 735, 10000, 54571):
        median_rank = (n + 1) // 2
        seq = [random() for _ in xrange(n)]
        found1 = _sort_select(median_rank, seq)
        found2 = select(median_rank, seq)
        if found1 != found2:
            print "Error, n, found1, found2:", n, found1, found2
    print "First tests finished. ------------------\n"

    n_repeats = 6
    print "n. repeats =", n_repeats
    print "len(list), min time select of 1 element:"
    for j in xrange(6, 21):
        n = 2 ** j
        deltas = []
        for i in xrange(n_repeats):
            seq = [random() for x in xrange(n)]
            nd2 = int(n // 2)
            t1 = clock()
            select(nd2, seq)
            #_sort_select(nd2, seq) # timsort
            t2 = clock()
            deltas.append(t2 - t1)
        print "2^%d = %d" % (j, n), "\t", round(1000*min(deltas), 3), "ms"


"""
Results on a PIII 500 MHz, Python 2.5.1, Windows:

Without Psyco:
n. repeats = 6
len(list), min time select of 1 element:
2^6 = 64        0.308 ms
2^7 = 128       0.715 ms
2^8 = 256       0.62 ms
2^9 = 512       2.808 ms
2^10 = 1024     6.339 ms
2^11 = 2048     11.578 ms
2^12 = 4096     18.251 ms
2^13 = 8192     53.954 ms
2^14 = 16384    105.219 ms
2^15 = 32768    140.378 ms
2^16 = 65536    281.057 ms
2^17 = 131072   733.205 ms
2^18 = 262144   1301.806 ms
2^19 = 524288   2791.104 ms
2^20 = 1048576  6676.635 ms


With Psyco:
n. repeats = 6
len(list), min time select of 1 element:
2^6 = 64        0.042 ms
2^7 = 128       0.083 ms
2^8 = 256       0.106 ms
2^9 = 512       0.175 ms
2^10 = 1024     0.418 ms
2^11 = 2048     0.95 ms
2^12 = 4096     2.41 ms
2^13 = 8192     5.946 ms
2^14 = 16384    15.197 ms
2^15 = 32768    44.098 ms
2^16 = 65536    65.942 ms
2^17 = 131072   186.058 ms
2^18 = 262144   348.069 ms
2^19 = 524288   555.882 ms
2^20 = 1048576  1489.913 ms


With _sort_select (timsort):
n. repeats = 6
len(list), min time select of 1 element:
2^6 = 64        0.102 ms
2^7 = 128       0.212 ms
2^8 = 256       0.474 ms
2^9 = 512       1.059 ms
2^10 = 1024     2.367 ms
2^11 = 2048     5.294 ms
2^12 = 4096     12.556 ms
2^13 = 8192     31.255 ms
2^14 = 16384    74.335 ms
2^15 = 32768    165.568 ms
2^16 = 65536    361.157 ms
2^17 = 131072   788.317 ms
2^18 = 262144   1738.317 ms
2^19 = 524288   3774.99 ms
2^20 = 1048576  8182.599 ms
"""