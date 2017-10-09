
import random

class explorationRobot:
    '''
    Defines how a Robot object is created
    '''
    __name = ''
    __pos = (2,2)
    __myWorld = None
    __perception = []
    __decision = None
    '''
    __perception = [('N',_),('S',_),('W',_), ('E',_)]
    '''
    __map = []
    '''
    __map =
            [_, N, _]
            [W, 0, E]
            [_, S, _]
    '''
    __mapWidth = 0
    __mapHeight = 0

    def cleanKnowledge(self):
        # Cleans the actual state of __decision and __perception
        self.__decision = None
        self.__perception = []

    def getName(self):
        return self.__name

    def setName(self, newName):
        assert isinstance(newName, str)
        self.__name = newName

    def getPos(self):
        return self.__pos

    def setPos(self, newPos):
        assert isinstance(newPos, tuple)
        self.__pos = newPos

    def getMyWorld(self):
        return self.__myWorld

    def getMap(self):
        return self.__map

    def setMapElem(self, elem, pos):
        assert not isinstance(elem, list)
        assert isinstance(pos, tuple)
        self.__map[pos[1]][pos[0]] = elem

    def delFirstMapColumn(self):
        for row in self.__map:
            del row[0]  # 0 for column 1, 1 for column 2, etc.

    def addFirstMapColumn(self, elem): # Creates a column of elems
        for row in self.__map:
            row.insert(0, elem)

    def delFirstMapRow(self):
        del self.__map[0]

    def addFirstMapRow(self, elem):
        lenght = len(self.getMap())
        newRow = [elem for i in range(lenght+1)]
        self.__map.insert(0, newRow)

    def delLastMapColumn(self):
        for row in self.__map:
            del row[-1]

    def addLastMapColumn(self, elem):
        for row in self.__map:
            row.insert(-1, elem)

    def delLastMapRow(self):
        del self.__map[-1]

    def addLastMapRow(self, elem):
        lenght = len(self.getMap())
        newRow = [elem for i in range(lenght+1)]
        self.__map.insert(-1, newRow)

    def mapPrint(self):
        for y in self.getMap():
            print(str(y))

    def getPerception(self):
        return self.__perception

    def setPerception(self, newPerception):
        assert all(isinstance(item, tuple) for item in newPerception)
        self.__perception = newPerception

    def getDecision(self):
        return self.__decision

    def setDecision(self, newDecision):
        assert isinstance(newDecision, tuple) and len(newDecision) == 2
        self.__decision = newDecision

    def __init__(self, name, mapWidth = 0, mapHeight = 0, world = None): # These are the height and the hight of robot vision
        assert isinstance(name, str)
        assert isinstance(mapWidth, int)
        assert isinstance(mapHeight, int)
        self.__name = name
        self.__pos = (int((mapWidth-1)/2), int((mapHeight-1)/2))
        self.__mapWidth = mapWidth
        self.__mapHeight = mapHeight
        self.__map = [ ['? ' for i in range(mapWidth)] for j in range(mapHeight) ]
        self.__myWorld = world

    def step(self):
        '''
        This is one step of the robot’s life
        :return: None
        '''
        self.sense()
        print('Robot Map: ')
        self.mapPrint()
        self.think()
        print('Robot Perception:')
        print(self.getPerception())
        print('Robot Decision: ')
        print(self.getDecision())
        self.act()

    def sense(self):
        # We can have sense, think and act methods
        self.perception(self.getMyWorld().getAround(self.getName()))

    def perception(self, sensors):
        '''
        build an internal model of the World given current sensors values
        :param sensors:
        :return: nothing, internal data only
        '''
        '''
        for s in sensors:
            if s[1] == ‘#’:
            # 2,2 è il centro
            if s[0] == ‘N’: self.map[1][2] = ‘#’
            elif s[0] == ‘S’: self.map[3][2] = ‘#’elif s[0] == ‘W’: self.map[2][1] = ‘#’
            else: self.map[2][3] = ‘#’
            # Or, better, se the following cycle:
        '''
        relativePosition = self.getPos()
        self.setMapElem(self.getName(), relativePosition)
        for s in sensors:
        # 2,2 è il centro
            if s[0] == 'N':
                coord = (2, 1)
                self.setMapElem(s[1], coord)
            elif s[0] == 'S':
                coord = (2, 3)
                self.setMapElem(s[1], coord)
            elif s[0] == 'W':
                coord = (1, 2)
                self.setMapElem(s[1], coord)
            else:
                coord = (3, 2)
                self.setMapElem(s[1], coord)
        self.setPerception(sensors)

    def think(self):
        self.decision(self.getPerception())

    def decision(self, possibleMoves):
        '''
        Partially random approach, we take a random empty ('0 ') cell or, if there aren't cells like this, a random visited cell
        :param possibleMoves
        :return: move to do
        '''
        goodMoves = [] # Moves to cells that are visited empty ('0 ')
        casualMove = None
        for m in possibleMoves:
            if m[1] == '0 ':
                goodMoves.append(m)
        if len(goodMoves) == 1:
            casualMove = goodMoves[0]
        elif len(goodMoves) > 1:
            casualMove = goodMoves[random.randrange(0, len(goodMoves)-1, 1)] # Chooses a random move from goodMoves (the ones that take to an empty cell)
        self.setDecision(casualMove)

    def act(self):
        self.makeMove(self.getDecision())

    def makeMove(self, move):
        assert isinstance(move, tuple) or move == None
        if move != None:
            actualPos = self.getPos()

            newPos = None
            self.getMyWorld().movingRobot(str(self.getName()), move[0]) # Notifies to the World to update his matrix
            if move[0] == 'N':
                newPos = (actualPos[0], actualPos[1] - 1)
                self.setMapElem(str(self.getName()), newPos)
                self.delLastMapRow()
                self.addFirstMapRow('? ')
            elif move[0] == 'S':
                newPos = (actualPos[0], actualPos[1] + 1)
                self.setMapElem(str(self.getName()), newPos)
                self.delFirstMapRow()
                self.addLastMapRow('? ')
            elif move[0] == 'W':
                newPos = (actualPos[0] -1 , actualPos[1])
                self.setMapElem(str(self.getName()), newPos)
                self.delLastMapColumn()
                self.addFirstMapColumn('? ')
            else:
                newPos = (actualPos[0] + 1, actualPos[1])
                self.setMapElem(str(self.getName()), newPos)
                self.delFirstMapColumn()
                self.addLastMapColumn('? ')
            self.cleanKnowledge()


    def __str__(self):
        return([self.getName, str(self.getPos())])
