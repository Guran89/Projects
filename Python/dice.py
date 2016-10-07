#coding=utf-8
import random, time

livskraft = 15
skromt = True

def atk(dmg, mod):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    resultat = roll1 + roll2 + mod
    print("Tärningarna visar: %d & %d" % (roll1, roll2))
    print("Resultat: %d" % (resultat))

    if resultat > 6:
        print("Attacken lyckades!")
        time.sleep(1)
        if resultat == 7:
            dmg_roll = random.randint(1, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du gör %d skada." % (atk_dmg))
        elif resultat == 8:
            dmg_roll = random.randint(2, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du gör %d skada." % (atk_dmg))
        elif resultat == 9:
            dmg_roll = random.randint(3, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du gör %d skada." % (atk_dmg))
        elif resultat > 9:
            dmg_roll = random.randint(4, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du gör %d skada." % (atk_dmg))
    else:
        print("Attacken missade.")

def defense(dmg, mod):
    global livskraft
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    resultat = roll1 + roll2 + mod
    print("Tärningarna visar: %d & %d" % (roll1, roll2))
    print("Resultat: %d" % (resultat))

    if resultat < 7:
        print("Du blev träffad!")
        time.sleep(1)
        if resultat == 6:
            dmg_roll = random.randint(1, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du tar %d skada." % (atk_dmg))
            livskraft = livskraft - atk_dmg
        elif resultat == 5:
            dmg_roll = random.randint(2, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du tar %d skada." % (atk_dmg))
            livskraft = livskraft - atk_dmg
        elif resultat == 4:
            dmg_roll = random.randint(3, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du tar %d skada." % (atk_dmg))
            livskraft = livskraft - atk_dmg
        elif resultat < 3:
            dmg_roll = random.randint(4, 6)
            atk_dmg = dmg_roll + dmg
            print("Skadetärningen visar: %d" % (dmg_roll))
            print("Du tar %d skada." % (atk_dmg))
            livskraft = livskraft - atk_dmg
    else:
        print("Du lyckades undvika!")

def status(life):
    print("Du har %d liv kvar." % life)

def quit():
    skromt = False

def actions():
    if action == atk:
        mod_input = input("Vad har du i attack?\n1T6+")
        dmg_input = input("Vad gör du i skada?\n1T6+")
        atk(dmg_input, mod_input)
    elif action == defense:
        dmg_input = input("Vad gör fienden i skada?\n1T6+")
        mod_input = input("Vad har du i undvika?\n1T6+")
        defense(dmg_input, mod_input)
    elif action == status:
        status(livskraft)
    elif action == quit:
        quit()
    else:
        print("Nu blev det fel.")

while skromt == True:
    action = input("\nVad vill du göra? (atk/defense/status):\n>")
    actions()
    if livskraft < 1:
        print("Du är död. Försök igen.")
        skromt = False
