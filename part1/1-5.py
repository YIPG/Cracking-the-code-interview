# 文字数変動が2以上だったらFlase
# 文字数変動が1のとき、文字種変動はS1(文字数おおいほう).pop(i for i in S1)==S2となる。
# 文字数変動がないとき、stringをリストとしみなすとS1,S2では一つの要素以外同じ。

import unittest


def arr_char(S1, S2):
    if len(S1) == len(S2):
        diff_count = 0
        for i in range(len(S1)):
            if S1[i] not in S2[i]:
                diff_count += 1
        if diff_count == 1:
            return True
        return False
    if abs(len(S1) - len(S2)) == 1:
        if len(S2) > len(S1):
            tmp = S2
            S2 = S1
            S1 = tmp
        S1_l = list(S1)
        for i in range(len(S1)):
            S1_l.pop(i)
            re_S1 = "".join(S1_l)
            if re_S1 == S2:
                return True
            S1_l = list(S1)
        return False
    return False


class Test(unittest.TestCase):
    dataT = [
        ("pale", "ple", True),
        ("tre", "true", True),
        ("truu", "true", True),  # u2,e0→u1,e1
        ("truu", "twue", False)  # u2, r1, w0, e0, u1, r0, w1, e1 文字の出現回数でカウントは意味ないか
    ]

    def test_arr_char(self):
        for [S1, S2, torf] in self.dataT:
            actual = arr_char(S1, S2)
            self.assertEqual(actual, torf)


if __name__ == "__main__":
    unittest.main()
