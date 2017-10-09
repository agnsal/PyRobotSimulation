import random

import Model.robot as robot

class Worls2D():
    __matrix = []
    __height = 1
    __width = 1
    __robotsInfo = {}


    def getHeight(self):
        return self.__height

    def setHeight(self, newHeight):
        assert isinstance(newHeight, int)
        self.__height = newHeight

    def getWidth(self):
        return self.__width

    def setWidth(self, newWidth):
        assert isinstance(newWidth, int)
        self.__width = newWidth

    def getRobotsInfo(self):
        return self.__robotsInfo

    def getRobot(self, name):
        assert type(name, str)
        if name in self.getRobotsInfo():
            return self.getRobotsInfo()['name']

    def addRobotInfo(self, newRobot, coordX, coordY):
        assert newRobot.__class__.__name__ == 'explorationRobot'
        assert isinstance(coordX, int)
        assert isinstance(coordY, int)
        self.__robotsInfo[str(newRobot.getName())] = {}
        self.__robotsInfo[str(newRobot.getName())]['robot'] = newRobot
        self.__robotsInfo[str(newRobot.getName())]['coordX'] = coordX
        self.__robotsInfo[str(newRobot.getName())]['coordY'] = coordY
        print(str(newRobot.getName()) + ' placed on: ' + str(coordX) + ', ' + str(coordY))

    def getMatrix(self):
        return self.__matrix

    def validMatrix(self, newMatrix): # Verify the newMatrix format
        assert isinstance(newMatrix, list)
        l = len(newMatrix[0])
        for row in newMatrix:
            if len(row) != l :
                return False
        return True

    def setMatrix(self, newMatrix):
        if self.validMatrix(newMatrix):
            self.__matrix = newMatrix
            self.setHeight(len(newMatrix))
            self.setWidth(len(newMatrix[0]))

    def setMatrixElem(self, elem, x, y):
        assert not isinstance(elem, list)
        assert isinstance(x, int)
        assert isinstance(y, int)
        self.__matrix[y][x] = elem

    def movingRobot(self, robName, direction):
        assert isinstance(robName, str)
        assert isinstance(direction, str)
        assert robName in self.getRobotsInfo()
        assert direction in ['N', 'S', 'E', 'W']
        robotInfo = self.getRobotsInfo()[robName]
        actualCoordX = robotInfo['coordX']
        actualCoordY = robotInfo['coordY']
        self.setMatrixElem('0 ', actualCoordX, actualCoordY)
        if direction == 'N':
            newCoordX = actualCoordX
            newCoordY = actualCoordY - 1
        elif direction == 'S':
            newCoordX = actualCoordX
            newCoordY = actualCoordY + 1
        elif direction == 'W':
            newCoordX = actualCoordX - 1
            newCoordY = actualCoordY
        else:
            newCoordX = actualCoordX + 1
            newCoordY = actualCoordY
        print('Robot is moving from (' + str(actualCoordX) + ', ' + str(actualCoordY) + ') to (' + str(newCoordX) + ', ' + str(newCoordY) + ')')
        robotInfo['coordX'] = newCoordX
        robotInfo['coordY'] = newCoordY
        self.setMatrixElem(robName, newCoordX, newCoordY)

    def getMatrixElem(self, x, y):
        assert isinstance(x, int)
        assert isinstance(y, int)
        if x < 0 or y < 0 or x > self.getWidth()-1 or y > self.getHeight()-1:
            return '- '
        return self.__matrix[y][x]

    def setRandomMatrix(self, matrixWidth, matrixHeight, wallsSparsity):
        assert isinstance(matrixWidth, int)
        assert isinstance(matrixHeight, int)
        assert isinstance(wallsSparsity, int)
        assert wallsSparsity > 1
        self.setMatrix([[0 for col in range(matrixHeight)] for row in range(matrixWidth)]) # Makes a 0s Matrix of matrixWidth*matrixHeight dimensions
        for x in range(matrixWidth):
            for y in range(matrixHeight):
                randomInt = random.randrange(1, wallsSparsity, 1) # randrange(start, stop, step)
                randomElem = '0 '
                if randomInt == wallsSparsity-1: # If randomInt is equal to the wallsSparsity-1 value (randomly obtainable), then randomElem is '#', that is a wall
                    randomElem = '# ' # P(#) = 1/wallsDensity
                self.setMatrixElem(randomElem, x, y)

    def worldPrint(self):
        for y in self.getMatrix():
            print(str(y))

    def makeRobots(self, robotsNumber, mapWidth, mapHeight):
        assert isinstance(robotsNumber, int)
        assert robotsNumber < self.getWidth()*self.getHeight()
        assert robotsNumber > 1
        for i in range(robotsNumber):
            randomX = random.randrange(0, self.getWidth()-1, 1)  # randrange(start, stop, step)
            randomY = random.randrange(0, self.getHeight()-1, 1)  # randrange(start, stop, step)
            self.setMatrixElem('R' + str(i), randomX, randomY)
            r = robot.explorationRobot('R' + str(i), mapWidth, mapHeight, self) # Creates a new robot Ri
            self.addRobotInfo(r, randomX, randomY)


    def getAround(self, robName):
        '''
        Extraction of the surroundings
        :param pos: coordinate of the central cell fron woch we extract the
        surroundings
        :return: list of surroundings cells
        '''
        assert isinstance(robName, str)
        assert robName in self.getRobotsInfo()
        robotInfo = self.getRobotsInfo()[robName]
        coordX = robotInfo['coordX']
        coordY = robotInfo['coordY']
        # (pos[0], pos[1]) = (x, y) is the cell the robot is placed into
        n = ('N', self.getMatrixElem(coordX, coordY - 1))
        s = ('S', self.getMatrixElem(coordX, coordY + 1))
        e = ('E', self.getMatrixElem(coordX + 1, coordY))
        w = ('W', self.getMatrixElem(coordX - 1, coordY))
        out = [n, s, e, w]
        return out