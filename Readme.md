Bienvenue dans le projet "Gestion de stock"! Ce projet est une application web Django conçue pour aider les entreprises à gérer leur inventaire de produits, leurs commandes et leurs livraisons.

## Fonctionnalités

L'application web "Gestion de stock" offre les fonctionnalités suivantes:

- Ajouter des produits.
- Ajouter des fournisseurs.
- Créer des commandes pour acheter des produits auprès des fournisseurs.
- Ajouter des produits à une commande et enregistrer les détails de la commande.
- Afficher la liste des commandes et leur statut.
- Générer des factures à partir des commandes.
- Ajouter des livraisons.

## Installation

Pour installer l'application web "Gestion de stock", suivez les étapes ci-dessous:

1. Clonez le dépôt Git de l'application web "Gestion de stock" en utilisant la commande suivante:

   ````
   git clone https://github.com/votre-nom-utilisateur/gestion-de-stock.git
   ```

2. Assurez-vous d'avoir Python 3.x et Django 3.x installés sur votre ordinateur.

3. Créez un environnement virtuel pour l'application web "Gestion de stock". Vous pouvez utiliser la commande suivante pour créer un nouvel environnement virtuel:

   ````
   python3 -m venv myenv
   ```

   Cette commande crée un nouvel environnement virtuel appelé "myenv".

4. Activez l'environnement virtuel en utilisant la commande suivante:

   ````
   source myenv/bin/activate
   ```

5. Installez les dépendances du projet en utilisant la commande suivante:

   ````
   pip install -r requirements.txt
   ```

6. Appliquez les migrations Django en utilisant la commande suivante:

   ````
   python manage.py migrate
   ```

7. Créez un utilisateur administrateur en utilisant la commande suivante:

   ````
   python manage.py createsuperuser
   
   database name : gestionStock
    user : anouar
    password : anouar2023[]
    ```


   Cette commande vous demandera de saisir un nom d'utilisateur, une adresse e-mail et un mot de passe pour l'utilisateur administrateur.

8. Lancez le serveur de développement Django en utilisant la commande suivante:

   ````
   python manage.py runserver
   ```

   Cette commande lancera le serveur de développement Django sur le port 8000 de votre ordinateur. Vous pouvez accéder à l'application web "Gestion de stock" en ouvrant un navigateur Web et en accédant à l'URL `http://localhost:8000`.

## Utilisation

Après avoir installé et lancé l'application web "Gestion de stock", vous pouvez l'utiliser pour gérer votre inventaire de produits, vos commandes et vos livraisons.

### Ajout de produits

Pour ajouter un nouveau produit, cliquez sur le lien "Produits" dans la barre de navigation, puis sur le bouton "Ajouter un produit". Remplissez le formulaire d'ajout de produit et cliquez sur le bouton "Enregistrer". Le nouveau produit sera ajouté à la liste des produits.

### Ajout de fournisseurs

Pour ajouter un nouveau fournisseur, cliquez sur le lien "Fournisseurs" dans la barre de navigation, puis sur le bouton "Ajouter un fournisseur". Remplissez le formulaire d'ajout de fournisseur et cliquez sur le bouton "Enregistrer". Le nouveau fournisseur sera ajouté à la liste des fournisseurs.

### Création de commandes

Pour créer une nouvelle commande, cliquez sur le lien "Commandes" dans la barre de navigation, puis sur le bouton "Créer une commande". Sélectionnez le fournisseur pour la nouvelle commande, puis ajoutez les produits requis à la commande. Enregistrez les détails de la commande en cliquant sur le bouton "Enregistrer". La nouvelle commande sera ajoutée à la liste des commandes.

### Génération de factures

Pour générer une nouvelle facture à partir d'une commande existante, cliquez sur le lien "Factures" dans la barre de navigation, puis sur le bouton "Générer une facture". Sélectionnez la commande pour laquelle vous souhaitez générer une facture, puis cliquez sur le bouton "Générer". La nouvelle facture sera ajoutée à la liste des factures.

### Ajout de livraisons

Pour ajouter une nouvelle livraison,cliquez sur le lien "Livraisons" dans la barre de navigation, puis sur le bouton "Ajouter une livraison". Sélectionnez la commande associée à la livraison, indiquez la quantité de produits livrés et enregistrez les détails de la livraison en cliquant sur le bouton "Enregistrer". La nouvelle livraison sera ajoutée à la liste des livraisons.

### Marquage des livraisons comme payées

Pour marquer une livraison comme payée, cliquez sur le lien "Livraisons" dans la barre de navigation, puis sur la livraison que vous souhaitez marquer comme payée. Cochez la case "Payée" et enregistrez les modifications en cliquant sur le bouton "Enregistrer". La livraison sera marquée comme payée dans la liste des livraisons.

## Conclusion

L'application web "Gestion de stock" est une solution simple et efficace pour gérer votre inventaire de produits, vos commandes et vos livraisons. Elle est facile à installer et à utiliser, et offre toutes les fonctionnalités dont vous avez besoin pour gérer votre entreprise. N'hésitez pas à l'essayer et à nous faire part de vos commentaires et suggestions d'amélioration!