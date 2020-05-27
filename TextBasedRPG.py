import os
import random

baseMap = [
  list("..S.."),
  list("....."),
  list("..E.."),
  list("....."),
  list(".....")
]
overworld = [
  list("..S.."),
  list("....."),
  list("..E.."),
  list("....."),
  list(".....")
]

#Player
playerHealth = 100
maxHealth = 100
strength = 10
randomStrength = random.randint(-3, 3)
playerExp = 0
x = 0
y = 0

g = 0
armour = 0
pots = 0
bombs = 0

#Enemies
enemyHealth = 50
randomEnemyStrength = random.randint(-2, 2)
enemyX = 0
enemyY = 0

while True:
  os.system("clear")
  overworld[y][x] = "P"
  for row in overworld:
    for c in  row:
      print(c, end = (" "))
    print("")
  overworld[y][x] = baseMap[y][x]

  print(f"You are at: {x}, {y}.\n")

  if baseMap[y][x] == "S":
    print("[1] Enter the Store?\n")
  elif baseMap[y][x] == 'E':
    print("You enter combat.")

    while True:
      randomStrength = random.randint(-3, 3)
      randomEnemyStrength = random.randint(-2, 2)

      print("What do you do?")
      print("[1] Attack\n[2] Item\n[3] Run")
      choice = input("Choice: ")

      if choice == "1":
        enemyHealth -= strength + randomStrength
        print(f"You deal {strength + randomStrength} damage")
        if enemyHealth <= 0:
          print("You killed the enemy!")
          randomG = random.randint(11, 19)
          g += randomG
          print(f"You earned {randomG}G\tYou have {g}G")
          playerExp += random.randint(1, 3)
          if playerExp >= 20:
            print("You levelled up!")
            maxHealth += 10
            playerHealth = maxHealth
            strength += 1
          enemyHealth = 50
          input("Press ENTER to continue")
          baseMap[y][x] = "."
          while True:
            enemyX = random.randint(0, 4)
            enemyY = random.randint(0, 4)
            baseMap[enemyY][enemyX] = "E"
            if baseMap[y][x] and baseMap[1][3] != "E":
              overworld[enemyY][enemyX] = baseMap[enemyY][enemyX]
              break
          break
        playerHealth -= (5 + randomEnemyStrength) - armour
        if playerHealth <= 0:
          print("You lose")
          exit()
        print(f"The enemy deals {(5 + randomEnemyStrength) - armour} damage\n")
        print(f"You have {playerHealth}HP\tThe enemy has {enemyHealth}HP\n")
        input("Press ENTER to continue")
        os.system("clear")
      
      elif choice == "2":
        os.system("clear")
        print("What item do you want to use?")
        print(f"[H]ealing Potion ({pots})\n[B]omb ({bombs})")
        choice = input("Choice: ").upper()

        if choice == "H" and pots > 0:
          pots -= 1
          playerHealth += 50
          if playerHealth > maxHealth:
            playerHealth = maxHealth
          print("You healed 50HP\n")
        elif choice == "B" and bombs > 0:
          bombs -= 1
          enemyHealth -= 20 + strength + randomStrength
          print(f"The bomb does {20 + strength + randomStrength} damage\n")
        input("Press ENTER to continue")
        os.system("clear")

      elif choice == "3":
        randomFlee = random.randint(1, 10)
        if randomFlee == 1:
          print("You failed to flee!")
          continue
        print("You flee the battle\n")
        input("Press ENTER to continue")
        baseMap[y][x] = "."
        while True:
          enemyX = random.randint(0, 4)
          enemyY = random.randint(0, 4)
          baseMap[enemyY][enemyX] = "E"
          if baseMap[y][x] and baseMap[1][3] != "E":
            overworld[enemyY][enemyX] = baseMap[enemyY][enemyX]
            break
        break
    continue
  
  print("Choose a direction to move in")
  print("[N]orth\n[S]outh\n[E]ast\n[W]est")
  choice = input("Choice: ").upper()

  if choice == "N":
    y -= 1
  elif choice == "S":
    y += 1
  elif choice == "E":
    x += 1
  elif choice == "W":
    x -= 1
  elif baseMap[y][x] == "S" and choice == "1":
    os.system("clear")
    print("You enter the store")
    while True:
      print("What do you want to do?")
      print("[1] Buy\n[2] Sell\n[3] Leave")
      choice = input("Choice: ")

      if choice == "1":
        while True:
          input("Press ENTER to continue")
          os.system("clear")
          if armour == 2:
            print(f"Buy...\t Your G: {g}\n10G [H]ealing Potion ({pots})\n10G [B]omb ({bombs})\n[E]xit")
          else:
            print(f"Buy...\t Your G: {g}\n50G [A]rmour\n10G [H]ealing Potion ({pots})\n10G [B]omb ({bombs})\n[E]xit")
          choice = input("Choice: ").upper()

          if choice == "A":
            if g < 50:
              print("You don't have enough G!")
              continue
            g -= 50
            armour = 2
          elif choice == "H":
            if g < 10:
              print("You don't have enough G!")
              continue
            g -= 10
            pots += 1
          elif choice == "B":
            if g < 10:
              print("You don't have enough G!")
              continue
            g -= 10
            bombs += 1
          elif choice == "E":
            os.system("clear")
            break

      elif choice == "2":
        while True:
          input("Press ENTER to continue")
          os.system("clear")
          print(f"Sell...\tYour G: {g}\n[H]ealing Potion ({pots})\n[B]omb ({bombs})\n[E]xit")
          choice = input("Choice: ").upper()

          if choice == "H":
            g += 10
            pots -= 1
          elif choice == "B":
            g += 10
            bombs -= 1
          elif choice == "E":
            os.system("clear")
            break
      elif choice == "3":
        break
