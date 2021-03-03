from unittest import TestCase


def triple_step(num):
    memo = dict()
    answer = helper(num, memo)
    return answer


def helper(num, memo):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    if num in memo:
        return memo[num]

    memo[num] = helper(num - 1, memo) + helper(num - 2, memo) + helper(num - 3, memo)
    return memo[num]


class Test(TestCase):
    def test001(self):
        self.assertEqual(triple_step(1), 1)

    def test002(self):
        self.assertEqual(triple_step(2), 2)

    def test003(self):
        self.assertEqual(triple_step(3), 4)

    def test004(self):
        self.assertEqual(triple_step(4), 7)


if __name__ == '__main__':
    TestCase.unittest.main()
