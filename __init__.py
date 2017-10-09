
import Model.world as world

chessboard = world.Worls2D()
chessboard.setRandomMatrix(10,10,10)
chessboard.makeRobots(3, 5, 5)
stepsNumber = 10

robotsInfo = chessboard.getRobotsInfo()
for s in range(stepsNumber):
    print('\n')
    print(' ++++++++++++++++++++ State ' + str(s) + ' ++++++++++++++++++++')
    chessboard.worldPrint()
    robotsInfo = chessboard.getRobotsInfo()
    for robI in robotsInfo:
        r = robotsInfo[robI]['robot']
        print('\n')
        print('---------- ' + r.getName() + ' ----------')
        r.step()
