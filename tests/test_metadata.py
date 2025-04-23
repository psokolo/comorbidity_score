import unittest
from comorbidity_score_calc.calc import calculate_score

class TestMetadataLoading(unittest.TestCase):
    def test_metadata_returned(self):
        score, categories, metadata = calculate_score(
            icd_codes=["EX1.1"],
            score="charlson",
            icd_version="icd10gm",
            year="2024",
            return_metadata=True
        )
        self.assertIsInstance(metadata, dict)
        self.assertIn("label", metadata)
        self.assertIn("source", metadata)
        self.assertEqual(metadata["label"], "Charlson Comorbidity Index")