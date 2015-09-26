import lenientcharset, harshcharset
import printSet, sys
#Given a class input string, and a RNG set(ex. 4d6 drop one, 3d6)
#Generates a set of random numbers and assigns them as the class desires

#Take an input string properly
def takeInput(outStr):
    inStr=None
    while not inStr:
        try:
            inStr=str(raw_input(outStr))
        except ValueError:
            print "Invalid choice."
    return inStr.lower()

#Roll the stats
def roll(rollStr):
    stats=[]
    rollCall=None
    rollDict=dict([
        
        ('3d6',harshcharset.gen),
        ('4d6b3',lenientcharset.gen)
        
        ])
    
    try:
        rollCall=rollDict[rollStr]
    except KeyError:
        print "Unable to find your roll options in the table."
        sys.exit()
    for i in range(0,6):
        stats.append(rollCall())
        
    print "Initial stats are:"
    for i in stats:
        print i
    return stats

#Given a class string, determine the stat order of it
#Note: classStr==is necessary - compare the values, not
#the identities - don't use "is"
#Sorceror/sorcerer is double in case users mispell it
def getStatsSet(classStr):
    statSet=None
    classDict=dict([ 

        ('barbarian',[0,2,1,5,3,4]),
        ('bard',[4,2,1,5,3,0]),
        ('cleric',[3,2,1,5,0,4]),
        ('druid',[5,1,2,4,0,3]),
        ('fighter',[0,3,1,4,2,5]),
        ('monk',[3,0,2,5,1,4]),
        ('paladin',[0,4,2,5,3,1]),
        ('ranger',[4,0,1,3,2,5]),
        ('rogue',[4,0,2,5,3,1]),
        ('sorcerer',[5,1,2,3,4,0]),
        ('sorceror',[5,1,2,3,4,0]),
        ('warlock',[5,1,2,4,3,0]),
        ('wizard',[5,1,2,0,3,4]),

         ])

    statSet=classDict.get(classStr)
    if statSet is None:
        print "Unable to find your class in the table."
        sys.exit()
    return statSet

#Assort the stats according to class preference(i.e. Wizard=Int first)
def assort(origStats,classOrder):
    arrangedStats=[0]*6
    for i in range(0,6):
        #Find the lowest remaining unused index of rangerOrder
        #Then place the highest remaining stat into that slot
        #In arrangedStats
        index=classOrder.index(i)
        arrangedStats[index]=max(origStats)
        origStats.remove(max(origStats))

    print
    print "Arranged stats are:"
    #Print out the char's stats nicely
    printSet.printnice(arrangedStats)

def main():
    print "Class options: Barbarian, Bard, Cleric, Druid, Fighter,"\
"Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard."
    classStr=takeInput("Enter a class name:")
    print "Roll options: 3d6, 4d6b3."
    rollStr=takeInput("Enter a roll option:")
    stats=roll(rollStr)
    classOrder=getStatsSet(classStr)
    assort(stats,classOrder)

main()
