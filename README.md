# Sujet 7 Gestion de trafic aérien

Ce sujet va vous permettre de fournir une interface de gestion du trafic aérien entre des aéroports. Le gestionnaire pourra ajouter des aéroports, des avions des vols des compagnies, … Le schéma de données est le suivant:

- des aéroports (id, nom, pays)
- des pistes d'atterrissages (numéro, aéroport, longueur)
- des compagnies (id, nom, description, pays de rattachement)
- des type d'avions (id, marques, modèle, description, images, longueur de piste nécessaire)
- des avions (id, nom, compagnie, modèle)
- des vols (id, avions, pilote, aéroport de départ,  date et heure de départ, aéroport d'arrivée, date et heure d'arrivée)

Vous devez implémenter un CRUD pour chacun de ces types de données. Vous préparerez la base en avance et la remplirez avec des aéroports, des pistes, des types d'avions, des compagnies, et des avions 

Votre site web devra permettre la saisie de nouveaux avions, des pistes et des vols. L'ajout de vol devra vérifier qu'il y a une piste compatible disponible à l'heure d'arrivée ou devra proposer un horaire plus tard (on comptera 10 minutes d'usage d'une piste par un avion avant qu'elle ne soit libre). Vous devrez aussi pouvoir insérer un ensemble de vols à partir d'un aéroport au travers d'un fichier. La structure du fichier attendu devra bien sur être décrite soit dans une aide, soit en préambule de la page de chargement.

Vous devrez être à même de pouvoir générer une fiche des vols prévus au départ d'un aéroport ou à destination d'un aéroport pour une date ou période données.

Pour cela vous aller créer un site web permettant d'alimenter, de consulter et de manipuler un schéma de données qui vous sera confié, correspondant à un besoin de votre entreprise. ce site web sera hébergé sur un service web que vous aurez mis en place et utilisera une base de données dont vous aurez installé et configuré de façon simple le serveur de gestion (un seul utilisateur de base).

Tous ces services seront installé déployer dans une machine virtuelle Linux que vous aurez configuré et dans laquelle vous aurez installé les composants nécessaires à votre développement et aux services utilisés.

votre projet étant collaboratif, vous utilisez des outils de travail collaboratif autant pour suivre le code que pour travailler sur les délivrables attendus à la fin du projet. Ces délivrables seront:

- Un planning, un diagramme de Gantt de votre projet (affection des taches, et temps)  (par groupe) 
- Une procédure d'installation et de déploiement de votre application web dans laquelle vous expliquerez la conception de votre solution (2-5 pages) (individuelle)
- Une fiche de projet dans votre portfolio personnel cette fiche contiendra aussi un résumé de la SAÉ en anglais (individuelle) 
- Une présentation rapide de votre projet par groupe (8 minutes de présentation/démo et 5 minutes de questions) (par groupe)
- Un dépôt GitHub de votre projet contenant tout le développement de votre application avec le schéma de données, le Gantt  (par groupe)
