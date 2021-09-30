"""
Implementation of the Vocabulary class
"""

import csv


class Vocabulary:
    def __init__(self, path: str) -> None:
        """Constructor.

        Args:
            path (str): Path to CSV file
        """
        self.path = path
        self.voc_e = {}
        self.voc_c = {}

        self.load_vocabulary()

    
    def load_vocabulary(self):
        with open(self.path, "r", encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                self.voc_e[row["english"]] = row["czech"]
                self.voc_c[row["czech"]] = row["english"]


    def translate(self, question: str) -> str:
        result = self.voc_e.get(question, "")
        if result == "":            
            result = self.voc_c.get(question, "")
        return result 
