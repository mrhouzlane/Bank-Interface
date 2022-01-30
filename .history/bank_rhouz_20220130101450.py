from abc import ABCMeta, abstractmethod
from random import randint
from client import Client
from exception import FirstEx, SecondEx
import eel

# class Account(metaclass=ABCMeta):
#     @abstractmethod
#     def creerCompte():
#         return 0

#     @abstractmethod
#     def connexion():
#         return 0

#     @abstractmethod
#     def retrait():
#         return 0

#     @abstractmethod
#     def deposer():
#         return 0

#     @abstractmethod
#     def Balance():
#         return 0


class Vault(Client):

    @eel.expose
    def __init__(self):
        # [key][0] => name ; [key][1] => password, [key][]
        super().__init__()
        self.bancaire = {}
        self.name = None
        self.montantRetrait = 0
        self.balance = 0
        self.montantDepot = 0

    @eel.expose
    def getNumAcc(self):
        return self.numAcc

    @eel.expose
    def displayInfo(self):
        if self.name != None:
            print("📓📓📓📓📓📓📓📓📓📓📓📓📓📓📓📓")
            print("Le nom du client est    : ", self.name)
            print("Le numéro de compte est : ", self.numAcc)
            print("Votre adresse email est : ",  self.getEmail())
            self.Balance()
            print("📓📓📓📓📓📓📓📓📓📓📓📓📓📓📓📓")

    @eel.expose
    def getEmail(self):
        return f'{self.name}@BANK-RHOUZLANE.com'

    @eel.expose
    def connexion(self, numAcc, password):
        print()
        if numAcc in self.bancaire.keys():
            if self.bancaire[numAcc][1] == password:
                print("Authentication réussie 🎉🎉🎉 !!!")
                self.numAcc = numAcc
                print()
                return True
            else:
                print(
                    "⚠️ Authentication échouée , veuillez entrer le bon mot de passe ⚠️ ")
                print()
                return False

    @eel.expose
    def retrait(self, montantRetrait):
        print()
        if montantRetrait > self.bancaire[self.numAcc][2]:
            raise FirstEx("Balance insuffisante")
        elif montantRetrait == self.bancaire[self.numAcc][2]:
            raise SecondEx(
                "Votre solde ne peut pas être nul, veuillez réessayer")
        else:
            self.bancaire[self.numAcc][2] -= montantRetrait
            print("Retrait réussi 🎉🎉🎉")
            self.Balance()
        print()

    @eel.expose
   def getmontantRetrait(self):
        return self.montantRetrait

    def deposer(self, montantDepot):
        print()
        self.bancaire[self.numAcc][2] += montantDepot
        print("Dépôt réussi 🎉🎉🎉")
        self.Balance()
        print()

    def getmontantDepot(self):
        return self.montantDepot

    def Balance(self):
        print("Votre solde est de : ",
              self.bancaire[self.numAcc][2])
