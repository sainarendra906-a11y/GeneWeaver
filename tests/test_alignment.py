
import unittest

from src.alignment.cpu_engine import find_alignments


class TestCPUAlignment(unittest.TestCase):

    def test_exact_match(self):
        result = find_alignments("ATCG", "GGATCG")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["position"], 2)
        self.assertEqual(result[0]["mismatches"], 0)

    def test_multiple_exact_matches(self):
        result = find_alignments("ATCG", "ATCGGGATCG", max_mismatches=0)
        self.assertEqual(len(result), 2)
        
    def test_one_mismatch(self):
        result = find_alignments("ATCG", "ATGG", 1)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["mismatches"], 1)

    def test_maximum_allowed_mismatches(self):
        result = find_alignments("ATCG", "GTAT", 3)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["mismatches"], 3)

    def test_reject_excessive_mismatches(self):
        result = find_alignments("AAAA", "TTTT", 3)
        self.assertEqual(len(result), 0)

    def test_case_insensitive_matching(self):
        result = find_alignments("atcg", "ATCG")
        self.assertEqual(len(result), 1)

    def test_empty_guide(self):
        with self.assertRaises(ValueError):
            find_alignments("", "ATCG")

    def test_empty_target(self):
        with self.assertRaises(ValueError):
            find_alignments("ATCG", "")

    def test_negative_mismatch_limit(self):
        with self.assertRaises(ValueError):
            find_alignments("ATCG", "ATCG", -1)

    def test_target_shorter_than_guide(self):
        result = find_alignments("ATCG", "AT")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
