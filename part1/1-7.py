import unittest

# 問題の意味がわからないが、とりあえず行列を90度回転させるメソッドを書く。
# テストから書き始めるの結構大事かも。
# numpyでやれよって思ったけど、numpyのメソッドなくてビビった。ほえほえ.

# 一回連結させて区切る？


def rotataion(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    result = []
    for i in range(columns):
        result.append([])
    for n in range(rows):
        for m in range(columns):
            result[columns - m - 1].append(matrix[n][m])
    return result


class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ], [
            [4, 8, 12],
            [3, 7, 11],
            [2, 6, 10],
            [1, 5, 9]
        ])
    ]

    def test_rotation(self):
        for matrix, answer in self.data:
            actual = rotataion(matrix)
            self.assertEqual(actual, answer)


if __name__ == "__main__":
    unittest.main()
