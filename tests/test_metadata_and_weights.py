import unittest
from comorbidity_score_calc.calc import calculate_score

class TestMetadataAndWeights(unittest.TestCase):

    def test_metadata_combined_return(self):
        score, categories, metadata = calculate_score(
            icd_codes=["B18.2"],
            score="charlson",
            icd_version="icd10gm",
            year="2024",
            weight_scheme="default",
            return_metadata=True
        )
        self.assertIn("mapping", metadata)
        self.assertIn("weights", metadata)
        self.assertIn("source", metadata["mapping"])
        self.assertIn("source", metadata["weights"])
        self.assertIn("doi", metadata["mapping"])

    def test_missing_weight_raises_error(self):
        with self.assertRaises(ValueError):
            # Assumes B18.2 matches a category that we intentionally omit from override
            calculate_score(
                icd_codes=["B18.2"],
                score="charlson",
                icd_version="icd10gm",
                year="2024",
                weights_override={"liver_mild": None}  # Simulate missing all weights
            )