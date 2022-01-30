from bank_rhouz import Vault
# import eel
# eel.init('static')
# eel.start('index.html', mode='chrome-app', port=8080,
#           cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

UserCase = Vault()
while True:
    print()
    print("💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰")
    print("💳   Welcome to RHOUZLANE Bank 2022   💳")
    print("💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰")
    print("👍 CHOIX 1 : Créer un compte")
    print("👍 CHOIX 2 : Accéder à votre compte")
    print("👍 CHOIX 3 : Afficher Informations de votre compte")
    print("👍 CHOIX 4 : Quitter")
    print()
    print()
    Choix = int(input())
    print()
    if Choix == 1:
        print()
        print("Entrez votre nom: ")
        name = input()
        print("Entrez un mot de passe: ")
        password = int(input())
        # print(UserCase.getEmail())
        # email = input()
        print("Entrez un montant de dépôt: ")
        deposer = int(input())
        UserCase.creerCompte(name, password, deposer)
        print()
    elif Choix == 2:
        print()
        print("Entrez votre numéro de compte: ")
        numAcc = int(input())
        print("Entrez votre mot de passe: ")
        password = int(input())
        statusConnexion = UserCase.connexion(numAcc, password)
        print()
        if statusConnexion == True:
            while True:
                print()
                print("Retrait  ▶️ APPUYER SUR 1 ✅")
                print("Déposer  ▶️ APPUYER SUR 2 ✅ ")
                print("Balance  ▶️ APPUYER SUR 3 ✅ ")
                print("MENU     ▶️ APPUYER SUR 4 ✅")
                Choix = int(input())
                print()
                if Choix == 1:
                    print()
                    print("Entrer un montant de retrait :")
                    montantRetrait = int(input())
                    UserCase.retrait(montantRetrait)
                    print()
                elif Choix == 2:
                    print()
                    print("Enter un montant à déposer :")
                    montantDepot = int(input())
                    UserCase.deposer(montantDepot)
                    print()
                elif Choix == 3:
                    print()
                    UserCase.Balance()
                    print()
                elif Choix == 4:
                    break
    elif Choix == 3:
        UserCase.displayInfo()
    elif Choix == 4:
        quit()
