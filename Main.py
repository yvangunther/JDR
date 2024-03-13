from POO_Function import joueur
from POO_Function import monstre
from POO_Function import actions
from POO_Function import room

player=joueur("myr",50,50,30,30,5,10,["Potion","Potion","Potion"],['Flash','Heal'],['Vamp'],[],30,0, 1,)
monster=monstre.generation_monster()


while player.hp > 0:
    actions().verif_stat(player)
    player.info_Player()
    
    print("Qu'allez-vous faire maintenant? Combat / Inventaire / Exploration / Leave")
    choix = input().lower()
    match choix:
      case "combat":
        actions().menu_combat(player,monster)
        if monster.hp <= 0:
          print(f"le {monster.name} disparait et vous obtenez {monster.exp} exp ")
          player.exp += monster.exp

      case  "inventaire":
        actions().inventaire(player)

      case  "exploration":
        actions().exploration()
      case  "leave":
        exit()
    
print("vous est mort selon vos choix")