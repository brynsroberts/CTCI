from unittest import TestCase


def power_set(lst):
    # list to store all subsets
    subsets = list()
    subsets.append([])

    # set to store tuples of seen sub lists
    memo = set()
    memo.add(())

    # call helper function
    helper(lst, subsets, memo)

    return subsets


def helper(lst, subsets, memo):
    # base case - lst contains no values
    # emtpy list already added to memo and subsets
    if len(lst) == 0:
        return

    # add currently seen lst to memo and subsets
    memo.add(tuple(lst))
    subsets.append(lst)

    # go through every variation of subsets and add if not in memo yet
    for i in range(len(lst)):
        new_lst = lst[0:i] + lst[i + 1:]
        if tuple(new_lst) not in memo:
            helper(new_lst, subsets, memo)


class Test(TestCase):
    def test001(self):
        lst = [1, 2, 3]
        rtn = [[1, 2, 3], [1, 2], [1, 3], [2, 3], [1], [2], [3], []]
        self.assertEqual(sorted(rtn), sorted(power_set(lst)), msg="test001")

    def test002(self):
        lst = []
        rtn = [[]]
        self.assertEqual(sorted(rtn), sorted(power_set(lst)), msg="test001")


if __name__ == '__main__':
    TestCase.unittest.main()
