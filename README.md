# Système de management Bancaire OOP - Python 

### Interface de l’application 

Le modèle bancaire de l’application RHOUZLANE Bank 2022 doit assurer les fonctionnalités ** suivantes à un client : 

```
1/ Créer un compte.
2/ Accéder à son compte et effectuer des opérations. 
3/Afficher les informations relatives à son compte. 
```

Pour cela, une interface doit être lisible et clair et permettre à un nouveau client de se retrouver. Elle devrait avoir un menu compatible avec les fonctionnalités décrites en **.  

Ainsi, pour créer un compte, il faudra à l’utilisateur fournir les informations suivantes : 

```
Nom : String  (exemple : “Mehdi”) 
Mot de passe : Integer (exemple : 202020)
Montant de dépôt initial qui peut être nul : (exemple : 500)
```
Ces données devront être stockés selon un numéro de compte qui permettra d’identifier chaque utilisateur d’un autre et qui sera crée aléatoirement et aura une valeur numérique entre comprise entre 1000000 et 9999999. 

Si les conditions ci-dessus sont valides, un message sera affiché et informera le client de la création de son nouveau compte délivré avec son numéro de compte. 

Pour accéder aux fonctionnalités de son comptes, un utilisateur devra fournir un numéro de compte et son mot de passe. L’interface lui informera de la réussite de l’authentification si mot de passe et compte correspondent. 

La plateforme devra afficher une interface graphique 2 à l’utilisateur les fonctionnalités proposées au client après connexion et seront les suivantes :
 ````
Retirer 
Déposer 
Vérifier Balance
Revenir au Menu
````
Le client devra pouvoir voir l’interface graphique 2 après chaque opération pour pouvoir poursuivre ses opérations.

Si le client choisit de retirer, il devra entrer une valeur numérique qui soit strictement supérieur à sa balance, le cas contraire se verra renvoyer un message d’erreur. 

Si le client choisit de déposer un montant, suite à sont dépôt il se verra afficher un message le félicitant de son dépôt et lui affichant son nouveau solde. 

Si le client choisit de voir son solde, il se verra afficher son solde. 

Dans le cas contraire aux 3 possibilités, le client peut choisir de revenir au MENU principal (interface graphique 1 ). 

L’interface doit également permettre au client de consulter ses informations et entre autre son numéro de compte, qu’il devra utiliser pour accéder à son compte. Pour cela, il pourra choisir d’afficher les informations de son compte qui devront afficher :
````
Son nom 
Son numéro de compte 
Sa nouvelle adresse email chez la banque 
Son solde 
````
Le cas échéant, il pourra choisir la 4ème option et quitter l’interface. 
