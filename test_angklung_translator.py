import unittest

from angklung_translator import translate_numbers, translate_to_all_keys


class AngklungTranslatorTest(unittest.TestCase):
    def test_translate_c_to_d(self):
        self.assertEqual(translate_numbers("1 2 3 4 5 6 7", "C", "D"), "b7 1 2 b3 4 5 6")

    def test_translate_with_rest_and_octave(self):
        self.assertEqual(translate_numbers("1+1 0 b7-1", "C", "C"), "1+1 0 b7-1")

    def test_translate_preserves_explicit_zero_octave(self):
        self.assertEqual(translate_numbers("1+0", "C", "C"), "1+0")

    def test_translate_to_all_keys_has_12_results(self):
        result = translate_to_all_keys("1 2 3", "C")
        self.assertEqual(len(result), 12)
        self.assertIn("F#", result)


if __name__ == "__main__":
    unittest.main()
