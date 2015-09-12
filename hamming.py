import itertools

def hamming(xs,ys):         # works on iterables of equal length
    if len(xs) != len(ys):
        raise ValueError(
            'Hamming distance not defined for sequences of unequal length')
    return sum(x != y for x,y in zip(xs,ys))  # in python True == 1, False == 0



def min_hamming(iterables): # can take any number of lists, tuples, or sets
                            # that contain lists, tuples, or strings
    accumulator = []
    for x,y in itertools.combinations(iterables,2):
        accumulator.append(hamming(x,y))
    return min(accumulator)




teststring1 = "abcdef"
teststring2 = "abcdeg"
teststring3 = "abcdzx"
teststring4 = "lmnopq"
testtuple1 = (1,2,3,4,5,6)
testtuple2 = (1,2,3,4,8,9)

assert hamming(teststring1,teststring1) == 0
assert hamming(testtuple1, testtuple1) == 0
assert hamming(teststring1, teststring2) == 1
assert hamming(teststring1, teststring4) == 6
assert hamming(testtuple1, testtuple2) == 2
assert hamming(teststring1, testtuple1) == 6

assert min_hamming((teststring1, teststring2, teststring3, teststring4)) == 1
assert min_hamming((teststring1, teststring3, teststring4)) == 2
