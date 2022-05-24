# Sujet 7 Gestion de trafic aérien

Ce sujet va vous permettre de fournir une interface de gestion du trafic aérien entre des aéroports. Le gestionnaire pourra ajouter des aéroports, des avions des vols des compagnies, … Le schéma de données est le suivant:

    des aéroports (id, nom, pays)
    des pistes d'atterrissages (numéro, aéroport, longueur)
    des compagnies (id, nom, description, pays de rattachement)
    des type d'avions (id, marques, modèle, description, images, longueur de piste nécessaire)
    des avions (id, nom, compagnie, modèle)
    des vols (id, avions, pilote, aéroport de départ,  date et heure de départ, aéroport d'arrivée, date et heure d'arrivée)

Vous devez implémenter un CRUD pour chacun de ces types de données. Vous préparerez la base en avance et la remplirez avec des aéroports, des pistes, des types d'avions, des compagnies, et des avions 

Votre site web devra permettre la saisie de nouveaux avions, des pistes et des vols. L'ajout de vol devra vérifier qu'il y a une piste compatible disponible à l'heure d'arrivée ou devra proposer un horaire plus tard (on comptera 10 minutes d'usage d'une piste par un avion avant qu'elle ne soit libre). Vous devrez aussi pouvoir insérer un ensemble de vols à partir d'un aéroport au travers d'un fichier. La structure du fichier attendu devra bien sur être décrite soit dans une aide, soit en préambule de la page de chargement.

Vous devrez être à même de pouvoir générer une fiche des vols prévus au départ d'un aéroport ou à destination d'un aéroport pour une date ou période données
