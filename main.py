"""
Albert Cloutier
406
tp4.3/enum
"""
from enum import Enum
from random import randint


class Alignement(Enum):
    loyal = 1
    chaotique = 2
    neutre = 3


def chiffres_eleves():
    valeurs = []
    for i in range(1, 4):

        valeur_de = randint(1, 6)
        valeurs.append(valeur_de)
    valeurs.sort()
    del valeurs[0]
    return sum(valeurs)


class Npc:
    def __init__(self, nom, race, espece, profession, alignement):
        self.Alignement = alignement

        self.force = chiffres_eleves()
        self.agilite = chiffres_eleves()
        self.constitution = chiffres_eleves()
        self.intelligence = chiffres_eleves()
        self.sagesse = chiffres_eleves()
        self.charisme = chiffres_eleves()
        self.armure = randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.point_de_vie = randint(1, 20)
        self.profession = profession

    def afficher_caracteristiques(self):
        print(f"l'alignement est {self.Alignement}")
        print(f"La valeur de la force est {self.force}")
        print(f"La valeur de l'agilité est {self.agilite}")
        print(f"La valeur de la constitution est {self.constitution}")
        print(f"La valeur de l'intelligence est {self.intelligence}")
        print(f"La valeur de la sagesse est {self.sagesse}")
        print(f"La valeur de la charisme est {self.charisme}")
        print(f"La valeur de l'armure est {self.armure}")
        print(f"Le nom est {self.nom}")
        print(f"La race est {self.race}")
        print(f"L'espèce est {self.espece}")
        print(f"Le nombre de points de vie est {self.point_de_vie}")
        print(f"La profession est {self.profession}")
    def attaque_statique(self):
        pass
    def est_vivant(self):
        pass


kobold1 = Npc("jean", "chien", "blanc", "ouvrier", 1)
kobold1.afficher_caracteristiques()
