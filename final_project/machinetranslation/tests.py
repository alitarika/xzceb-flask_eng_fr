""" author: alitarika - Tarik // tests of translations w/ unittest """
import unittest
from translator import englishtofrench, frenchtoenglish

class Testenglishtofrench(unittest.TestCase):
    def testenfr(self):
        self.assertEqual(englishtofrench(" ")," ") # test1 en fr
        self.assertEqual(englishtofrench("Hello"),"Bonjour") #test 2 en fr hello and bonjour
        self.assertEqual(englishtofrench("Yes"),"Oui") # test 3 en fr yes and oui
        self.assertNotEqual(englishtofrench("Yes"), "Yes") # null test yesfr=yes

class Testfrenchtoenglish(unittest.TestCase):
    def testfren(self):
        self.assertEqual(frenchtoenglish(" ")," ") # test 1 fr en
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello") # test 2 fr en bonjour and hello
        self.assertEqual(frenchtoenglish("Oui"),"Yes") # test 3 fr en oui and yes
        self.assertNotEqual(frenchtoenglish("Oui"), "Oui") # null test ouien=yes

unittest.main()