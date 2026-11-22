from numba import cuda


@cuda.jit
def alignment_kernel(guide, target, results, guide_length, target_length):
    index = cuda.grid(1)

    if index < target_length - guide_length + 1:
        mismatches = 0

        for j in range(guide_length):
            if guide[j] != target[index + j]:
                mismatches += 1

        results[index] = mismatches