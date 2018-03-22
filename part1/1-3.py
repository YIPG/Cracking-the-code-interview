import unittest


def URLify(S , length):
    return S.replace(" ", "%20")


# TODO:Test書かなあかん
text = "google  ha sugoi kamo"
L = len(text)
print(URLify(text,L))

# 3/21 テスト書いた
class Test(unittest.TestCase):
    data = [
        ('overwatch love  is strong', 25,
         'overwatch%20love%20%20is%20strong'),
        ('kakuno mendo', 12,
        'kakuno%20mendo')
    ]

    def test_urlify(self):
        for [test_string, length, answer] in self.data:
            conv = URLify(test_string, length)
            self.assertEqual(conv, answer)


if __name__ == "__main__":
    unittest.main()
