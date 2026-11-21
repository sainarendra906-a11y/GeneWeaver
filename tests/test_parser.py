import tempfile
import unittest
from pathlib import Path

from src.parser.fasta_parser import parse_fasta


class TestFastaParser(unittest.TestCase):

    def test_multiple_sequences(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fasta_file = Path(temp_dir) / "sample.fasta"
            fasta_file.write_text(
                ">gene_001\nATGC\n>gene_002\nGCTA\n"
            )

            result = parse_fasta(fasta_file)

            self.assertEqual(len(result), 2)
            self.assertEqual(result[0]["id"], "gene_001")
            self.assertEqual(result[1]["id"], "gene_002")

    def test_sequence_length(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fasta_file = Path(temp_dir) / "sample.fasta"
            fasta_file.write_text(">gene_001\nATGCGT\n")

            result = parse_fasta(fasta_file)

            self.assertEqual(result[0]["length"], 6)
            self.assertEqual(result[0]["sequence"], "ATGCGT")

    def test_empty_fasta(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            fasta_file = Path(temp_dir) / "empty.fasta"
            fasta_file.write_text("")

            result = parse_fasta(fasta_file)

            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
