from random import randint
import random

#########################

list_loot=[["Potion",15,12],["Fiole",15,12]]
list_monstre=[["Slime",1],["Squelette",1],["Mimic",1],["fantome",1],["Gargouille",2],["Chevalier sans tête",2],["Master hand",2],["Liche",3],["Bishop",3]]
list_decor = ["debris de vers","menotte ronger par le temps","rien","des os brisé"]


#########################

class joueur:
    
    def __init__(self,name,maxHp,hp,maxMana,mana,armure,esquive,inventaire,sorts,buffs,debuffs,maxExp,exp,niveau):
        self.name = name
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
        self.armure = armure
        self.esquive = esquive
        self.inventaire = inventaire
        self.sorts = sorts
        self.buffs = buffs
        self.debuffs = debuffs
        self.maxExp = maxExp
        self.exp = exp
        self.niveau = niveau
    
    def info_Player (self):
        print(f"\n#Life : {self.hp}/{self.maxHp}\n#Mana : {self.mana}/{self.maxMana}\n#Buff : {self.buffs}\n#Debuff : {self.debuffs}\n#exp : {self.exp}/{self.maxExp}")




class monstre:
    
    def __init__(self,name,maxHp,hp,maxMana,mana,armure,esquive,inventaire,sorts,buffs,debuffs,exp,):
        self.name = name
        self.maxHp = maxHp
        self.hp = hp
        self.maxMana = maxMana
        self.mana = mana
        self.armure = armure
        self.esquive = esquive
        self.inventaire = inventaire
        self.sorts = sorts
        self.buffs = buffs
        self.debuffs = debuffs
        self.exp = exp

    def generation_monster():
        # Choisir un monstre aléatoire dans list_monstre
        monster_name, monster_strength = random.choice(list_monstre)

        # Déterminer les caractéristiques du monstre en fonction de sa force
        if monster_strength == 1:
            max_hp = random.randint(20, 25)
            max_Mana = random.randint(15, 25)
            armure = random.randint(3, 4)
            exp = random.randint(7, 12)
        elif monster_strength == 2:
            max_hp = random.randint(50, 65)
            max_Mana = random.randint(30,50)
            armure = random.randint(4, 7)
            exp = random.randint(13, 20)
        elif monster_strength == 3:
            max_hp = random.randint(75, 100)
            max_Mana = random.randint(60, 75)
            armure = random.randint(8, 12)
            exp = random.randint(25, 50)
        
        # Instancier et retourner un objet monstre avec les caractéristiques déterminées
        return monstre(monster_name, max_hp, max_hp, max_Mana, max_Mana, armure, 10, [], [], [], [], exp)

list_room=[[0, False, False, "premier salle", monstre]]
class room:
    
    def __init__(self,index,coffre,marchant,elements,monstre):
        self.index = index
        self.coffre = coffre
        self.marchant = marchant
        self.elements = elements
        self.monstre = monstre

    @staticmethod
    def generate_room(self):
        idList=self.index
        index_room = idList(list_room)
        index=index+1
        coffre_present = random.choice([True, False])
        marchand_present = random.choice([True, False])
        monstre_inst = monstre.generation_monster()
        description = random.choice(list_decor)

        return room(index, coffre_present, marchand_present, description, monstre_inst)
        


class actions:

    def verif_stat (self,player):          
        if player.hp > player.maxHp:  
            player.hp = player.maxHp
        if player.mana > player.maxMana:  
            player.mana = player.maxMana 

    def menu_combat(self,player,monster):
        print(f"Vous tombez sur un {monster.name}")
        print("Le combat commence ...")
        print("\n")
        choix = "null"

        while player.hp > 0 and monster.hp > 0:
            player.info_Player()
            
            print("Qu'allez-vous faire maintenant? Attaque / Inventaire / Spells ")
            choix_en_combat = input().lower()

            if choix_en_combat == "attaque":
                actions().Attack(player,monster)
            
            elif choix_en_combat  == "inventaire":
                actions().inventaire(player)

            elif choix_en_combat  == "spells":
                actions().use_spells_player(player,monster)

            if monster.hp > 0:
                actions().Attack(monster,player)

    def Attack(self, attacker, target):
        touched = random.randint(1, 20)
        if touched >= target.armure:
            atk_point = random.randint(1, 6)
            print(f"{attacker.name} frappe et inflige {atk_point} de dégâts")
            target.hp -= atk_point
            # Vérification des buffs de l'attaquant
            for buff in attacker.buffs:
                if buff == 'Vamp':
                    vampirise = round(atk_point * 0.13)
                    attacker.hp += vampirise
                    print(f"Vampirise vous fait récupérer {vampirise} points de vie")
                    actions().verif_stat(attacker)
                if buff == 'Death_touch':
                    target.hp = 0
                    print("le doua la touché")
        else:
            print('Raté')


    def exploration(self,current_room):
        print("Exploration d'une nouvelle salle ? oui/non")
        choix = input().lower()
        if choix == "oui":
            # Génération de la pièce suivante
            new_room = current_room.generate_room(current_room.index + 1)  
            print(f"Salle actuelle : {new_room.index}")
            print(f"Description de la pièce : {new_room.elements}")
            print(f"Un monstre apparaît : {new_room.monstre.name}")

    

    def inventaire(self):
        print("Accès à l'inventaire")
        items_counts = {}
        for item in self.inventaire:
            if item in items_counts:
                items_counts[item] += 1
            else:
                items_counts[item] = 1
        for item, count in items_counts.items():
            if count > 1:
                print(f'{count}x {item}')
            else:
                print(item)
        choix = input("Quel objet voulez-vous utiliser ? Entrez le nom de l'objet ou 'annuler' pour revenir : ")
        if choix.lower() == "annuler":
            print("Opération annulée.")
            return
        found = False
        for item, count in items_counts.items():
            if item.lower() == choix.lower():
                found = True
                print(f"Usage de {item}")
                if item == "Potion" and self.hp < self.maxHp :
                    self.inventaire.remove(item)
                    self.hp +=15
                if item == "Fiole" and self.mana < self.maxMana :
                    self.inventaire.remove(item)
                    self.mana +=15
                break
        if not found:
            print("Nom de l'objet inconnu ou aucun exemplaire en stock")


    def use_spells_player(self, attacker, target):
        for spells in attacker.sorts:
            print(f'-- {spells}')
        choix_spell = input().lower()
        match choix_spell:
            case "flash":
                if target.hp > 0:
                    if attacker.mana > 10:
                        attacker.mana -= 10
                        for _ in range(3):
                            actions().Attack(attacker, target)
                else:
                    print('aucune cible disponible')
                    
            case 'heal':
                if attacker.mana >= 10:
                    attacker.mana -=10
                    attacker.hp+=12
                    print('Vous recuperer 12 hp')
                    actions().verif_stat(attacker)
            case _:
                print ('Nom du sort inconnu')

class event:
    def marchand ():
        print ("un marchand est dans la salle")