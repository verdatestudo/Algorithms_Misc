
'''
Different ways of generating permutations and combinations

Last Updated: 2016-May-23
First Created: 2016-May-20
Python 2.7
Chris
'''

import itertools

def itools_perm(my_string):
    '''
    Returns len(my_string)! results (e.g 4! = 24)
    '''
    for item in itertools.permutations(my_string):
        print item

def perm2(my_string):
    '''
    Recursive implementation of permutations.
    '''
    result = []

    if len(my_string) <= 1:
        return my_string
    else:
        for idx, item in enumerate(my_string):
            for perm in perm2(my_string[:idx] + my_string[idx+1:]):
                result.append(item + perm)

    return result

def itools_combo(my_string, num_of_letters):
    '''
    Returns n!/r! * (n - r)! results (e.g 4, 3 = 4! / 3! * 1 = 24 / 6 = 4)
    '''
    for item in itertools.combinations(my_string, num_of_letters):
        print item

def choose_sets(mylist, length):
    '''
    Recursive implementation of combinations.
    '''
    mylen = len(mylist)

    if length == mylen:
        return [mylist]
    elif length == 1:
        return [[i] for i in mylist]
    elif length > mylen:
        return []

    results = []
    for k in xrange(mylen):
        if mylen - k + 1 > length:
            for j in choose_sets(mylist[k+1:], length - 1):
                new_combo = [mylist[k]]
                new_combo.extend(j)
                results.append(new_combo)
    return results

def test():
    '''
    run
    '''
    my_string = 'abcd'
    itools_perm(my_string)
    print perm2(my_string)
    itools_combo(my_string, 3)
    print choose_sets(my_string, 3)
