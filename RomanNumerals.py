"""
(1) Given a string representing a Roman numeral, write a function to compute the Arabic numerical equivalent.
For example roman_to_arabic("MDCCLXXVI") should return 1776.
"""
import unittest


class RomanNumerals:
    def __init__(self):
        self.roman_nums = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

        self.set_roman_nums = self.roman_nums.keys()
        self.sequence_roman_nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    def check_value_of_numeral_begins_5(self, x: int) -> bool:
        while x > 10:
            x = x / 10
        return x == 5

    def check_valid_numeral(self, char) -> bool:
        return char in self.set_roman_nums

    def get_value_from_char(self, char) -> int:
        return self.roman_nums[char]

    def check_chars_within_two(self, char_1, char_2) -> bool:
        index_1 = self.sequence_roman_nums.index(char_1)
        index_2 = self.sequence_roman_nums.index(char_2)
        if abs(index_1 - index_2) <= 2:
            return True
        return False

    """
    Evaluates a roman numeral in one pass and returns the value, or -1 if invalid.
    This problem would have been easier to solve by running multiple passes; I wanted to challenge myself and see if
    I could do it in one. In a production environment--unless I'm expecting heavy use or long roman numerals--I would
    run multiple passes for clarity's sake.
    """
    def roman_numeral_into_decimal(self, numeral: str) -> int:
        if len(numeral) == 0:
            return 0

        total = 0
        cur_char = None
        cur_value = 0
        next_char = None
        next_value = 0
        num = 0
        max_val = float("inf")
        total_from_cur_numeral = 0
        set_new_cur_char = True
        while num < len(numeral):
            if set_new_cur_char:
                set_new_cur_char = False
                total_from_cur_numeral = 0
                cur_char = numeral[num]
                if not self.check_valid_numeral(cur_char):
                    return -1
                cur_value = self.get_value_from_char(cur_char)
            if num < len(numeral)-1:
                next_char = numeral[num+1]
                if not self.check_valid_numeral(next_char):
                    return -1
                next_value = self.get_value_from_char(next_char)
                if next_value >= cur_value:
                    if self.check_value_of_numeral_begins_5(cur_value):
                        return -1
                if next_value > cur_value:
                    if not self.check_chars_within_two(cur_char, next_char):
                        return -1
                    cur_value = -cur_value
                    amount_to_add = cur_value + next_value
                    num += 1
                    set_new_cur_char = True
                    if amount_to_add > max_val:
                        return -1
                    max_val = abs(cur_value) - 1
                else:
                    amount_to_add = cur_value
                    total_from_cur_numeral += cur_value
                    if amount_to_add > max_val:
                        return -1
                    max_val = cur_value
                    if next_value < cur_value:
                        if total_from_cur_numeral > cur_value * 3 and cur_value != 1000:
                            return -1
                        total_from_cur_numeral = 0
            else:
                amount_to_add = cur_value
                if amount_to_add > max_val:
                    return -1
                total_from_cur_numeral += cur_value
                if total_from_cur_numeral > cur_value * 3 and cur_value != 1000:
                    return -1
            total += amount_to_add
            cur_char = next_char
            cur_value = next_value
            num += 1
        return total


class TestCases(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCases, self).__init__(*args, **kwargs)
        self.roman_numerals_object = RomanNumerals()

    def test_basic_calculation(self):
        self.assertEqual(1776, self.roman_numerals_object.roman_numeral_into_decimal("MDCCLXXVI"))
        self.assertEqual(1, self.roman_numerals_object.roman_numeral_into_decimal("I"))
        self.assertEqual(3724, self.roman_numerals_object.roman_numeral_into_decimal("MMMDCCXXIV"))
        self.assertEqual(9, self.roman_numerals_object.roman_numeral_into_decimal("IX"))
        self.assertEqual(6, self.roman_numerals_object.roman_numeral_into_decimal("VI"))
        self.assertEqual(45, self.roman_numerals_object.roman_numeral_into_decimal("XLV"))
        self.assertEqual(555, self.roman_numerals_object.roman_numeral_into_decimal("DLV"))
        self.assertEqual(5000, self.roman_numerals_object.roman_numeral_into_decimal("MMMMM"))
        self.assertEqual(99, self.roman_numerals_object.roman_numeral_into_decimal("XCIX"))

    def test_illegal_char(self):
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("ABC"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("MDCCLZXXVI"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("MDCCLXXVIZ"))

    def test_empty_string(self):
        self.assertEqual(0, self.roman_numerals_object.roman_numeral_into_decimal(""))

    def test_numerals_out_of_order(self):
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("IVXXLCCDM"), -1)
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("VIX"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("VX"))

    def test_impossible_combinations(self):
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("XCX"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("IXVI"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("IC"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("VC"))

    def test_too_many_repeating(self):
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("DD"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("XXXX"))
        self.assertEqual(-1, self.roman_numerals_object.roman_numeral_into_decimal("XXXXI"))

if __name__ == '__main__':
    unittest.main()
