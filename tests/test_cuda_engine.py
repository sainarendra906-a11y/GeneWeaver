import unittest
import numpy as np
from numba import cuda

from src.gpu.cuda_engine import alignment_kernel


class TestCUDAAlignment(unittest.TestCase):

    def test_alignment_kernel(self):
        guide = np.array([65, 84, 67, 71], dtype=np.uint8)
        target = np.array(
            [71, 71, 65, 84, 67, 71, 84, 65, 84, 67, 71],
            dtype=np.uint8
        )

        guide_length = len(guide)
        target_length = len(target)

        results = np.zeros(target_length, dtype=np.int32)

        threads_per_block = 32
        blocks = (target_length + threads_per_block - 1) // threads_per_block

        alignment_kernel[blocks, threads_per_block](
            guide,
            target,
            results,
            guide_length,
            target_length
        )

        expected = [4, 4, 0, 4, 4, 3, 4, 0]

        self.assertEqual(
            results[:len(expected)].tolist(),
            expected
        )


if __name__ == "__main__":
    unittest.main()