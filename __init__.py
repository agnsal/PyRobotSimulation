
'''
Copyright 2017-2018 Agnese Salutari.
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on 
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and limitations under the License
'''

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
