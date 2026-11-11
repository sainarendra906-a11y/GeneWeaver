
from Bio import SeqIO


def parse_fasta(file_path):
    sequences = []

    for record in SeqIO.parse(file_path, "fasta"):
        gene = {
            "id": record.id,
            "sequence": str(record.seq),
            "length": len(record.seq)
        }

        sequences.append(gene)

    return sequences


if __name__ == "__main__":
    genome = parse_fasta("data/sample.fasta")

    for gene in genome:
        print("Gene ID:", gene["id"])
        print("Length:", gene["length"])
        print("Sequence:", gene["sequence"])
        print("-" * 40)

    print("Total sequences:", len(genome))
