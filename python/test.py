import unittest
from solution.solution import solution
from solution.process_files import read_books, process_string


class TestSolution(unittest.TestCase):
    maxDiff = None

    def test_simple_case(self):
        simple_data = {
            "unique sentence": "Unique words are the only ones that should appear because they are unique.",
            "common sentence": "Common words shouldn't appear at all. Because they are common.",
            "rare sentence": "Rare words are the most valuable. Because they are rare.",
        }

        processed_data = {
            key: process_string(value) for key, value in simple_data.items()
        }

        self.assertEqual(
            solution(processed_data, 1),
            {
                "unique sentence": ["unique"],
                "common sentence": ["common"],
                "rare sentence": ["rare"],
            },
        )

    def test_books(self):
        book_data = read_books()
        expected_data = {
            "A Doll's House.txt": [
                "nora",
                "helmer",
                "linde",
                "krogstad",
                "torvald",
                "christine",
                "nils",
                "goodnight",
                "skylark",
                "tarantella",
            ],
            "A Modest Proposal.txt": [
                "publick",
                "breeders",
                "kingdom",
                "hath",
                "infants",
                "jonathan",
                "computed",
                "landlords",
                "carcass",
                "annum",
            ],
            "A Tale of Two Cities.txt": [
                "lorry",
                "defarge",
                "manette",
                "pross",
                "carton",
                "darnay",
                "lucie",
                "cruncher",
                "monsieur",
                "monseigneur",
            ],
            "Alice's Adventures in Wonderland.txt": [
                "alice",
                "turtle",
                "hatter",
                "gryphon",
                "dormouse",
                "caterpillar",
                "mouse",
                "dinah",
                "cats",
                "dodo",
            ],
            "Frankenstein.txt": [
                "clerval",
                "justine",
                "felix",
                "geneva",
                "frankenstein",
                "safie",
                "elizabeth",
                "agatha",
                "mountain",
                "mon",
            ],
            "Metamorphosis.txt": [
                "gregor",
                "samsa",
                "grete",
                "charwoman",
                "onto",
                "violin",
                "metamorphosis",
                "alright",
                "broom",
                "immobile",
            ],
            "Pride and Prejudice.txt": [
                "darcy",
                "bennet",
                "bingley",
                "wickham",
                "collins",
                "lydia",
                "lizzy",
                "gardiner",
                "elizabeth",
                "longbourn",
            ],
            "The Adventures of Sherlock Holmes.txt": [
                "holmes",
                "sherlock",
                "lestrade",
                "rucastle",
                "mccarthy",
                "inspector",
                "coronet",
                "clair",
                "hosmer",
                "turner",
            ],
            "The Great Gatsby.txt": [
                "gatsby",
                "jordan",
                "tom",
                "daisy",
                "wolfshiem",
                "garage",
                "myrtle",
                "buchanan",
                "michaelis",
                "wilson",
            ],
            "The Importance of Being Earnest.txt": [
                "algernon",
                "cecily",
                "gwendolen",
                "bracknell",
                "prism",
                "worthing",
                "chasuble",
                "bunbury",
                "merriman",
                "cardew",
            ],
        }
        output_data = solution(book_data, 10)
        for key, value in expected_data.items():
            # Order of the top ten words is not tested
            self.assertCountEqual(output_data[key], value)


if __name__ == "__main__":
    unittest.main()
