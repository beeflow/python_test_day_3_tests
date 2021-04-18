"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
import unittest

from colorama import Fore, Style
from unittest_data_provider import data_provider

from bobs import bobs_count
from dict_to_tuple import dict_to_tuple
from lace_strings import lace_strings
from longest_alphabetical_substring import longest_alphabetical_substring
from primes_list import primes_list
from unique_values import unique_values


def print_ok(given, expected):
    print("[ ", Fore.GREEN + "OK", Style.RESET_ALL, "]", f"\ngiven: {given}\nexpected: {expected}\n", end="\n")


def print_fail(given, expected, actual):
    print("[ ", Fore.RED + "NO", Style.RESET_ALL, "]", f"\ngiven: {given}\nexpected: {expected}\nactual: {actual}\n",
          end="\n")


class FinalTest(unittest.TestCase):
    """
    Testy do zrobienia przez kursantów.

    https://www.startupjobs.pl/test/python
    """
    POINTS = 0
    MAX_POINTS = 0

    data_set_dict_to_tuple = lambda: (
        ([{"a": {"b": "c"}}, ("a", ("b", "c"))],),
        ([{"a": {"b": {"c": "d"}}}, ("a", ("b", ("c", "d")))],),
        ([{"a": {"b": {"c": "d"}}, "e": "f"}, ("a", ("b", ("c", "d")), "e", "f")],),
    )

    bobs_test_data_set = lambda: (
        (["nbcuobobobobbseobmqzbbobbobbbobboboboobo", 8],),
        (["oboovobbobbhbv", 1],),
        (["oobobafboboboobobobbbobobobobknvbobbi", 10],),
        (["coboboeoboborboobobibobbfdobim", 4],),
        (["oboboblcbobblb", 3],),
        (["bobobobobolovbobpobobozobobbbobb", 8],),
        (["bobboboooboboux", 3],),
        (["xkbiuoxjzkagsa", 0],),
        (["bobobobobobobobobob", 9],),
        (["bokgbohbojvbobobxobobobboobhbobby", 5],),
        (["bobobtbobobbobbobobyoobobbbbojfpuboobqobob", 9],),
        (["oboboboboboobobpodbobb", 6],),
        (["oboombobobobboobibhbobbbobbobzobob", 7],),
    )

    longest_alphabetical_substring_dp = lambda: (
        (["vppxqascolaidedhgrmst", "ppx"],),
        (["kmrstcqheo", "kmrst"],),
        (["cbasxwndaekga", "asx"],),
        (["jillkngr", "ill"],),
        (["ujmfvohumndokh", "jm"],),
        (["gyhelrmjcfpszivhrsmekjrn", "cfpsz"],),
        (["keaodfedqqmjwsyfrt", "dqq"],),
        (["abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"],),
        (["fwlqwskwucsvyrlqm", "csvy"],),
        (["ageckzhldbitkepkjdksl", "ckz"],),
        (["tarmxuhrobyhjufqyacsenml", "hju"],),
        (["zyxwvutsrqponmlkjihgfedcba", "z"],),
        (["waoegaxqvzk", "qvz"],),
    )

    lace_strings_dp = lambda: (
        ([["abcd", "efghi"], "aebfcgdhi"],),
        ([["abcdjkl", "efghi"], "aebfcgdhjikl"],),
        ([["abcd", "efghijkl"], "aebfcgdhijkl"],),
    )

    primes_list_dp = lambda: (
        ([2, [2]],),
        ([43, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]],),
        ([79, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]],),
        ([6, [2, 3, 5]],),
        ([11, [2, 3, 5, 7, 11]],),
    )

    unique_values_dp = lambda: (
        ([{1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}, [1, 3, 8]],),
        ([{1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0, 12: 9, 11: 7}, [1, 3, 8, 11, 12]],),
        ([{1: 1, 2: 1, 3: 1}, []],),
    )

    @staticmethod
    def check(expected, actual):
        try:
            assert expected == actual
            FinalTest.POINTS += 1
        except AssertionError:
            pass

        FinalTest.MAX_POINTS += 1

    def tearDown(self) -> None:
        print(f"total {FinalTest.POINTS} / {FinalTest.MAX_POINTS}")

    @data_provider(data_set_dict_to_tuple)
    def test_dict_to_tuple(self, test_cases):
        actual = dict_to_tuple(test_cases[0])
        self.check(test_cases[1], actual)

    @data_provider(bobs_test_data_set)
    def test_bobs(self, test_cases):
        actual = bobs_count(test_cases[0])
        self.check(test_cases[1], actual)

    @data_provider(longest_alphabetical_substring_dp)
    def test_longest_alphabetical_substring(self, test_cases):
        actual = longest_alphabetical_substring(test_cases[0])
        self.check(test_cases[1], actual)

    @data_provider(lace_strings_dp)
    def test_lace_strings(self, test_cases):
        actual = lace_strings(test_cases[0][0], test_cases[0][1])
        self.check(test_cases[1], actual)

    @data_provider(primes_list_dp)
    def test_primes_list(self, test_cases):
        actual = primes_list(test_cases[0])
        self.check(test_cases[1], actual)

    @data_provider(unique_values_dp)
    def test_unique_values(self, test_cases):
        actual = unique_values(test_cases[0])
        self.check(test_cases[1], actual)


if __name__ == '__main__':
    unittest.main()