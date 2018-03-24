# これは日本語では問題が意味不。

import unittest

def isSubstring(S1,S2):
    if S1 in S2:
        return True
    return False

def once_isSubstring(S1,S2):
    return isSubstring(S2, S1+S1)

class Test(unittest.TestCase):
    data=[
    ("abcdefg", "defgabc",True),
    ("coffeebottle", "bottledcoffe", False)
    ]
    def test_once_isSubstring(self):
        for [s1,s2,torf] in self.data:
            actual=once_isSubstring(s1,s2)
            self.assertEqual(actual,torf)
if __name__=="__main__":
    unittest.main()
