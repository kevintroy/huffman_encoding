import itertools

def hamming(s1,s2):         # works on strings or lists/tuples/sets of strings
    if not s1 or not s2:
        return 0
    else:
        d = 0
        if s1[0] != s2[0]:
            d += 1
        return d + hamming(s1[1:],s2[1:])

def min_hamming(iterables):  # can take any number of lists, tuples, or sets
                             # that contain lists, tuples, or strings
    accumulator = []
    
    for i in iterables:
        comparisons = set(iterables)
        comparisons.discard(i)

        for c in comparisons:
            accumulator.append(hamming(c,i))

    return min(accumulator)
