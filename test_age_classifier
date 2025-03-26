import unittest
from age_classifier import classify_age

class TestAgeClassifier(unittest.TestCase):
    def test_infant(self):
        # Testing boundary conditions for infant classification.
        # Ages 0 and 1 should both return "infant".
        self.assertEqual(classify_age(0), "infant")
        self.assertEqual(classify_age(1), "infant")
    
    def test_child(self):
        # Testing classification for children.
        # Ages greater than 1 and less than 13 should return "child".
        self.assertEqual(classify_age(2), "child")
        self.assertEqual(classify_age(12), "child")
    
    def test_teenager(self):
        # Testing classification for teenagers.
        # Ages between 13 and 19 should return "teenager".
        self.assertEqual(classify_age(13), "teenager")
        self.assertEqual(classify_age(19), "teenager")
    
    def test_adult(self):
        # Testing classification for adults.
        # Ages 20 and above should return "adult".
        self.assertEqual(classify_age(20), "adult")
        self.assertEqual(classify_age(35), "adult")
    
    def test_negative_age(self):
        # Testing that providing a negative age correctly raises a ValueError.
        with self.assertRaises(ValueError):
            classify_age(-1)

if __name__ == "__main__":
    unittest.main()
