from unittest import TestCase


def magic_index(lst):
    return helper(lst, 0, len(lst) - 1)


def helper(lst, left, right):

    # no more elements to look at - return -1
    if left > right:
        return -1

    # get middle element
    mid = (right + left) // 2
    val = lst[mid]

    # val matches index - return index
    if val == mid:
        return mid

    # if val is larger than its index, then index will never be able to match the right side
    # look at the left side
    elif val > mid:
        return helper(lst, left, mid - 1)

    # if val is smaller than the index, then the index will never be able to match the left side
    # look at the right side
    else:
        return helper(lst, mid + 1, right)


class Test(TestCase):
    def test001(self):
        lst = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
        self.assertEqual(magic_index(lst), 7, msg="test001")

    def test002(self):
        lst = [-1, 0, 1, 3]
        self.assertEqual(magic_index(lst), 3, msg="test002")

    def test003(self):
        lst = []
        self.assertEqual(magic_index(lst), -1, msg="test003")

    def test004(self):
        lst = [1, 2, 3, 4, 5, 6]
        self.assertEqual(magic_index(lst), -1, msg="test004")

    def test005(self):
        lst = [-6, -5, -4, -3, -2, -1]
        self.assertEqual(magic_index(lst), -1, msg="test005")

    def test006(self):
        lst = [-40, -20, -1, 1, 2, 3, 6, 8, 9, 12]
        self.assertEqual(magic_index(lst), 6, msg="test006")


if __name__ == '__main__':
    TestCase.unittest.main()
