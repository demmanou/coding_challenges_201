import unittest


# Given a integer, find the sequence of operations
# required to reach that number starting with 1
# The operations allowed are adding 5 and multiplying by 3
# For example 6 can be reached by adding 5 to 1 so the solution
# would be '1 + 5'. For 13 the solution would be '1 * 3 + 5 + 5'.
# If no solution is possible, return an empty string
# You're asked to find the fastest solution


class Solution:
    def sequence_to_number(self, num: int) -> str:
        pass


class Test(unittest.TestCase):
    test_cases = [
        (6, '1 + 5'),
        (13, '1 * 3 + 5 + 5'),
        (15, ''),
    ]

    test_functions = [
        Solution().sequence_to_number
    ]

    def test_funcs(self):
        for input_, expected in self.test_cases:
            for func in self.test_functions:
                output = func(input_)
                assert output == expected, \
                    f'\nFailed for input {input_}\nYour output: {output}\nCorrect output: {expected}'


if __name__ == "__main__":
    unittest.main()
