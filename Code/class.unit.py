class Unit():
    
    Abilities = {}
    FactionKeyword = []
    BasicLoadout = [] # To be used with the 'standard' armament for each unit.  Only referenced in an unmodified unit.
    Keyword = []
    Weapons = []
    ## I feel like I should be able to clump these variables into something cleaner.. .maybe a dictionary of lists?
    UnitIsPsyker = False
    UnitNumberOfPowersKnown = 0
    UnitNumberOfPowers = 0
    UnitNumberofDenials = 0
    UnitPsychicDiscipline = ''
    UnitPsykerPowersKnown = {}
    ## UnitPsykerCapabilities = [(UnitIsPsyker, False), (UnitNumberOfPowersKnown, 0), (UnitNumberOfPowers, 0), (UnitNumberOfDenials, 0), (UnitPsychicDiscipline, ''), (UnitPsykerPowersKnown, {})]
    CostPerModel = 0
    PowerCost = {} # formatted: "# of models: # power cost, #: #"
    UnitType = ''
    UnitIsUnique = False
    UnitComposition = {} # used if it's more than a single model.  Format should be: base: #, option1: #, option2: #.
        
    def __init__(self, Name, M, WS, BS, S, T, W, A, Ld, Sv):
        self.Name = Name # The Unit's Name
        self.M = M # movement characteristic
        self.WS = WS # weapon skill characteristic
        self.BS = BS # ballistic skill characteristic
        self.S = S # strength characteristic
        self.T = T # toughness characteristic
        self.W = W # wounds characteristic
        self.A = A # attacks characteristic
        self.Ld = Ld # leadership characteristic
        self.Sv = Sv # save characteristic

    ## The following methods are meant to display the unit's basic information, not for any modification purposes.

    def displayUnitStatBlock(self): # display the unit's basic stat block line.
        print("#################################")
        print("# Name: {}      #".format(self.Name))
        print("# M  WS  BS  S  T  W  A  Ld  Sv #")
        print("# {}  {}+  {}+  {}  {}  {}  {}  {}   {}+ #"
                .format(self.M,self.WS,self.BS,self.S,self.T,self.W,self.A,self.Ld,self.Sv))
        print("#################################")
    
    def displayUnitEchelonData(self):
        print("#################################")
        print("# " + self.Name + ' is a ' + self.UnitType + ' Unit. #')
        if self.UnitIsUnique == True:
            print("# " + self.Name + ' is a single model. #')
            print("# " + self.Name + '\'s point cost is ' + str(self.CostPerModel) + '. #')
            for value in self.PowerCost.values():
                print("# " + self.Name + '\'s power rating is ' + str(value) + '. #')
            
        else:
            print("# " + self.Name + '\'s point cost is ' + str(self.CostPerModel) + '.')
            print("# " + self.Name + '\'s base power rating is ' + str(self.PowerCost) + '.')
        print("#################################")
    
    def displayUnitAbilityBlock(self):
        print("#################################")
        print("#          Abilities            #")
        print("#################################")
        for key, value in self.Abilities.items():
            print("# " + key + "\n" + "#  " + value)
        print("#################################")
        
    def displayUnitBasicLoadout(self):
        print("# {} is armed with ".format(self.Name) + ', '.join(self.BasicLoadout) + ".")
    
    # not even sure if this should be a method.
    def displayUnitWeaponsBlock(self):
        print("# {} is armed with ".format(self.Name) + ', '.join(self.Weapons) + ".")
    
    def displayUnitPsykerAbilities(self):
        if self.UnitIsPsyker == True:
            print("# " + self.Name + ' can attempt to manifest ' + str(self.UnitNumberOfPowers) + ' Psychic powers in each friendly Psychic phase, and attempt to deny ' + str(self.UnitNumberOfDenials) + ' psychic powers in each enemy Psychic phase.  ' + self.Name + ' knows the Smite power and two psychic powers from the ' + self.UnitPsychicDiscipline + ' discipline.')
        else:
            pass
    
    def displayUnitKeywordBlock(self):
        print("#################################")
        print("# Faction Keywords: " + ', '.join(self.FactionKeyword))
        print("# Keywords: " + ', '.join(self.Keyword))
        print("#################################")

    ## the following methods are meant to allow changes to be made to a unit's information.  Not really sure how to implment this section.
    
    ## a method for reviewing the available unit-size options (how many models a unit is allowed to have.)
    ## a method for adding models to a unit.
    ## a method for subtracting models from a unit.
    ## a method for reviewing the weapons available to each model (should there be a different method for the squad leader?
    ## a method for adding weapons to a unit/model.
    def addUnitWeapons(self):
        
        pass
    ## a method for subtracting weapons from a unit/model.
    

# Sample unit to test-out class code.
GreyKnight1 = Unit('Lord Kaldor Draigo', 5, 2, 2, 4, 4, 7, 5, 9, 2)
Unit.displayUnitStatBlock(GreyKnight1)
GreyKnight1.CostPerModel = 240
GreyKnight1.PowerCost.update({1: 12})
GreyKnight1.UnitType = 'Headquarters'
GreyKnight1.UnitIsUnique = True
Unit.displayUnitEchelonData(GreyKnight1)
GreyKnight1.BasicLoadout.extend(['Storm Bolter', 'Titansword', 'Frag Grenade', 'Krak Grenade', 'Psyk-out Grenade'])
Unit.displayUnitBasicLoadout(GreyKnight1)
GreyKnight1.Abilities.update({'And They Shall Know No Fear' : 'You can re-roll failed Morale tests for this unit.', 'Daemon Hunters' : 'If this unit attacks any DAEMONS in the Fight phase, you can re-roll all failed wound rolls for those attacks.', 'Rites of Banishment' : 'When this unit manifests the Smite psychic power, it has a range of 12" rather than 18", and the target unit suffers only 1 mortal wound rathern than D3 (whether or not the result of the Psychic test is more than 10) - unless the target unit is a DAEMON, in which case it suffers 3 mortal wounds instead of D3.'})
Unit.displayUnitAbilityBlock(GreyKnight1)
GreyKnight1.UnitIsPsyker = True
GreyKnight1.UnitNumberOfPowersKnown = 2
GreyKnight1.UnitNumberOfPowers = 2
GreyKnight1.UnitNumberOfDenials = 2
GreyKnight1.UnitPsychicDiscipline = 'Sanctic'
GreyKnight1.UnitPsykerPowersKnown.update({'Purge Soul' : 'Purge Soul has a warp charge value of 5. If manifested, pick a visible enemy unit within 12" of the psyker. Both controlling players roll a dice and add their respective unit’s highest Leadership value. If the target’s total is equal to or greater than the psyker’s total, nothing happens. If the psyker’s total is greater than the target’s total, the target unit suffers a number of mortal wounds equal to the difference.', 'Gate of Infinity' : 'Gate of Infinityhas a warp charge value of 6. If manifested, pick a friendly GREY KNIGHTSunit within 12" of the psyker. Remove that unit from the battlefield and immediately set it up anywhere on the battlefield that is more than 9" from any enemy models.' })
Unit.displayUnitPsykerAbilities(GreyKnight1)
GreyKnight1.FactionKeyword.extend(['Imperium', 'Adeptus Astartes', 'Grey Knights'])
GreyKnight1.Keyword.extend(['Character', 'Infantry', 'Grand Master', 'Terminator', 'Psyker', 'Lord Kaldor Draigo'])
Unit.displayUnitKeywordBlock(GreyKnight1)