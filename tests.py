import unittest
from program import *


class MyTests(unittest.TestCase):
    
    def test_dodaj_abc(self):
        self.assertEqual(dodaj_abc(5,6,7), 18)
    
    def test_przywitanie(self):
        self.assertEqual(przywitanie(imie = "Amelia"), "Dzień dobry Amelia")
    
    def test_pole_kola(self):
        self.assertEqual(pole_kola(5), 78.5)