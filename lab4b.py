#!/usr/bin/env python3

def join_lists(l1, l2):
    # Use union of sets to combine unique elements, then convert back to list
    return list(set(l1).union(set(l2)))

def match_lists(l1, l2):
    # Return a list that contains all values found in both l1 and l2
    return list(set(l1).intersection(l2))

def diff_lists(l1, l2):
    # Return a list that contains all values not shared between both lists
    return list(set(l1).symmetric_difference(set(l2)))

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))


