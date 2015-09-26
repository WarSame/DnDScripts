import sys
def printnice(stats):
    if (len(stats) != 6):
        sys.exit("You need 6 stats.")
    print("Strength: %i" % stats[0])
    print("Dexterity: %i"%stats[1])
    print("Constitution: %i"%stats[2])
    print("Intelligence: %i"%stats[3])
    print("Wisdom: %i"%stats[4])
    print("Charisma: %i" %stats[5])
