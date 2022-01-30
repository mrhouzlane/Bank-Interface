from doctest import UnexpectedException
from unittest import mock, TestCase
import unittest
from bank_rhouz import Vault
from exception import FirstEx, SecondEx

# import pytest


# @pytest.fixture
# def setup_case_a():
#     BB = Vault()
#     # setup account for customer 234
#     BB.creerCompte(name="Mehdi", password=20, initialdeposer=200)
#     return BB


class LearnTest(unittest.TestCase):

    def test_creerCompte(self):
        # Arrange
        a = "Mehdi"
        b = 20
        c = 200
        # Act
        result = Vault()
        # Assert
        self.assertEqual(result.creerCompte(
            "Mehdi", 20, 200), [a, b, c])

    def test_conenxion(self):
        result = Vault()
        # Arrange
        a = "Mehdi"
        b = 20
        c = 200
        e = result.creerCompte(a, b, c)
        # Act
        # Assert
        self.assertEqual((result.connexion(result.getNumAcc(), b)), True)

    def test_deposer(self):
        result = Vault()
        a = "Mehdi"
        b = 20
        c = 200
        e = result.creerCompte(a, b, c)
        f = result.connexion(result.getNumAcc(), b)
        d = result.deposer(200)
        # Act
        # Assert
        self.assertEqual(result.Balance(), d)

    def test_retrait(self):
        result = Vault()
        a = "Mehdi"
        b = 20
        c = 200
        e = result.creerCompte(a, b, c)
        f = result.connexion(result.getNumAcc(), b)
        d = result.retrait(50)
        # Act
        # Assert
        self.assertEqual(result.Balance(), d)

    def test_get_email(self):
        result = Vault()
        # Arrange
        a = "MehdiRhouzlane"
        b = 20
        c = 200
        e = result.creerCompte(a, b, c)
        self.assertEqual("MehdiRhouzlane@BANK-RHOUZLANE.com",
                         result.getEmail())
        print(result.getEmail())

    def test_invalid_password(self):
        result = Vault()
        a = "Mehdi"
        b = 20  # mot de passe
        e = 45  # faux mot de passe
        c = 200
        e = result.creerCompte(a, b, c)
        self.assertEqual(result.connexion(result.getNumAcc(), e), False)

    def test_exception1(self):
        result = Vault()
        a = "Mehdi"
        b = 20
        c = 200  # Balance
        d = 500  # montant du retrait > Balance : 500>200
        e = result.creerCompte(a, b, c)
        f = result.connexion(result.getNumAcc(), b)
        #self.assertRaises(MyExcept, SecondEx, result.retrait, d)
        with self.assertRaises(FirstEx, msg=" Ressayez !! ") as context:
            result.retrait(d)
        print(context.exception)

    def test_exception2(self):
        result = Vault()
        a = "Mehdi"
        b = 20
        c = 200  # Balance
        d = 500  # montant du retrait > Balance : 500>200
        e = result.creerCompte(a, b, c)
        f = result.connexion(result.getNumAcc(), b)
        #self.assertRaises(MyExcept, SecondEx, result.retrait, d)
        with self.assertRaises(SecondEx, msg=" Ressayez !! ") as context:
            result.retrait(c)
        print(context.exception)


if __name__ == '__main__':
    unittest.main()


# class TestVault(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print('setupClass')

#     @classmethod
#     def tearDownClass(cls):
#         print('teardownClass')

#     # def SetUp(self):
#     #     print('setUp')
#     #     self.user1 = Vault()

#     def tearDown(self):
#         print('tearDown\n')

#     def test_creerCompte(self):
#         self.assertEqual(self.user1.name, self.Vault[self.numAcc][0])


# if __name__ == '__main__':
#     unittest.main()
