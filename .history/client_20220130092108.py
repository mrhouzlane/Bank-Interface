from random import randint


class Client:

    def creerCompte(self, name, password, balance):
        print()
        self.name = name
        self.balance = balance
        self.numAcc = randint(10000, 99999)
        self.password = password
        self.bancaire[self.numAcc] = [name, password, balance]
        print("🎉🎉🎉 Création de compte réussie  🎉🎉🎉  \n 💳 Le numéro du compte de {} est le {} 💳 ".format(
            self.name, self.numAcc))
        print()
        return self.bancaire[self.numAcc]
