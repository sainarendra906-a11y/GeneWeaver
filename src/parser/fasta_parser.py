from Bio import SeqIO

def parse_fasta(file_path):
    sequences = []

    with open(file_path, "r") as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
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