
def find_alignments(guide, target, max_mismatches=3):
    guide = guide.upper()
    target = target.upper()

    if not guide or not target:
        raise ValueError("Guide and target cannot be empty")

    if max_mismatches < 0:
        raise ValueError("Maximum mismatches cannot be negative")

    guide_length = len(guide)
    results = []

    for i in range(len(target) - guide_length + 1):
        window = target[i:i + guide_length]

        mismatches = sum(
            1 for a, b in zip(guide, window)
            if a != b
        )

        if mismatches <= max_mismatches:
            results.append({
                "position": i,
                "matched_sequence": window,
                "mismatches": mismatches
            })

    return results


if __name__ == "__main__":
    guide = "ATCG"
    target = "GGATCGTATCG"

    matches = find_alignments(guide, target)

    for match in matches:
        print(match)
