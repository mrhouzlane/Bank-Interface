from bank_rhouz import Vault
import eel
eel.init('static')
eel.start('index.html', mode='chrome-app', port=8080,
          cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])

UserCase = Vault()
while True:
    print()
    print("π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°")
    print("π³   Welcome to RHOUZLANE Bank 2022   π³")
    print("π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°π°")
    print("π CHOIX 1 : CrΓ©er un compte")
    print("π CHOIX 2 : AccΓ©der Γ  votre compte")
    print("π CHOIX 3 : Afficher Informations de votre compte")
    print("π CHOIX 4 : Quitter")
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
        print("Entrez un montant de dΓ©pΓ΄t: ")
        deposer = int(input())
        UserCase.creerCompte(name, password, deposer)
        print()
    elif Choix == 2:
        print()
        print("Entrez votre numΓ©ro de compte: ")
        numAcc = int(input())
        print("Entrez votre mot de passe: ")
        password = int(input())
        statusConnexion = UserCase.connexion(numAcc, password)
        print()
        if statusConnexion == True:
            while True:
                print()
                print("Retrait  βΆοΈ APPUYER SUR 1 β")
                print("DΓ©poser  βΆοΈ APPUYER SUR 2 β ")
                print("Balance  βΆοΈ APPUYER SUR 3 β ")
                print("MENU     βΆοΈ APPUYER SUR 4 β")
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
                    print("Enter un montant Γ  dΓ©poser :")
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
