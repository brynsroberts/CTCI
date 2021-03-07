from unittest import TestCase


def recursive_multiply(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    min_num = min(num1, num2)
    max_num = max(num1, num2)
    seen = dict()
    seen[1] = max_num
    return helper(max_num, min_num, 1, seen)


def helper(num1, num2, curr, seen):
    if num2 - curr in seen:
        return seen[num2 - curr] + seen[curr]

    # no point of saving larger numbers now
    elif num2 - curr < curr:
        curr_save = curr
        sum = 0
        target = num2 - curr
        curr = int(curr / 2)
        while target not in seen:
            if curr > 1:
                curr = int(curr / 2)
            else:
                curr = 1
            target = target - curr
            sum += seen[curr]
        return sum + seen[target] + seen[curr_save]

    seen[curr + curr] = seen[curr] + seen[curr]
    return helper(num1, num2, curr + curr, seen)


class Test(TestCase):
    def test001(self):
        self.assertEqual(12, recursive_multiply(3, 4), msg="test001")

    def test002(self):
        self.assertEqual(12, recursive_multiply(4, 3), msg="test002")

    def test003(self):
        self.assertEqual(0, recursive_multiply(0, 3), msg="test002")

    def test004(self):
        self.assertEqual(0, recursive_multiply(4, 0), msg="test002")

    def test005(self):
        self.assertEqual(1126611, recursive_multiply(453,2487), msg="test002")


if __name__ == '__main__':
    TestCase.unittest.main()
