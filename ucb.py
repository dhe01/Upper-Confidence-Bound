import random
import math
from array import *
from copy import deepcopy
import numpy as np
from checkers import checkers

class ucb:
    
    # initialize the board (position = starting position)
    def __init__(self, position = [1] * 12 + [0] * 8 + [-1] * 12, explore_param = math.sqrt(2)):
        
        self.position = position
        self.children = []
        self.explore_param = explore_param
        
        self.num_visits = 0
        
        self.actions = []
        self.UCBVals = []
        self.qHats = []
        self.qBars = []
        
        self.vHat = []
        self.optimalActions = []
        
        self.setActions()        
        self.actions = []
        self.UCBs = []
        self.qHats = []
        self.qBars = []
        self.numSamples = []
        
        self.vHat = 0
        
        self.optimalActions = []
        
        self.setActions()
        
    position = [1] * 12 + [0] * 8 + [-1] * 12
    children = []
    exploreParam = math.sqrt(2)
    numVisits = 0
    
    actions = []
    UCBs = {}
    qHats = {}
    qBars = {}
    numSamples = []
    
    vHat = 0
    
    optimalActions = []
    
    def validMoves(self, player):
        # Check valid moves using checkers class in checkers.py
        # states = checkers(position = self.position, player)
        # states.updateLocations()
        # self.actions = states.actions
        # return(self.actions)
        ""
        
    def init2(self):
        # Run after determining all possible actions
        # for action in self.actions:
        #    self.qHats[action] = 0
        #    self.qBars[action] = 0
        #    self.UCBs[action] = 0
        ""
    
    # Heuristic to prevent bad rollouts
    def boardEvaluator(self):
        # return(f(self.position)), where f denotes heuristic (likely use checkers.pawns and checkers.kings)
        ""
        
    def winCheck(self, player):
        # states = checkers(position = self.position, player)
        # states.updateLocations()
        
        # Win state
        # if position.count(-1) == 0:
        #     return(1)
        
        # Loss state
        # if position.count(1) == 0:
        #     return(0)
        
        # Tie state
        # if states.checkTie():
        #     return(1/2)
        
        # Undetermined
        # return(-1)
        ""
    
    # Randomly selects an opponent action unless optimal move
    def opponentAction(self):
        # states = checkers(position = self.position, player = 2)
        # states.updateLocations()
        
        # opponentActions = []
        # win = False
        # for move in states.actions:
        #     if self.winCheck((move on self).positions(), 2) == 1:
        #         if win:
        #             opponentActions.append(move)
        #         else:
        #             opponentActions=[move]
        #     elif not win:
        #         if self.winCheck(move on self.positions(), 2) != 0:
        #             opponentActions.append(move)
        
        # return(random.choice(opponentActions))
        ""
        
    def update(self, action, depth, depthBudget):
        # Simulate next moves:
        # position =  (move on self).positions()
        # opponentMove = self.opponentAction(position)
        # position = (opponent move on self).positions()
        
        # Create childstate based on resulting position
        # childState = ucb(positions = position)
        
        # If we want to create a tree
        # if depth > 1:
        #     for sample in range(depthBudget[depth-1]):
        #         childState.tree(depth - 1, depthBudget)
        # Otherwise
        # else:
        #     childState.tree(0, depthBudget)
        
        # Update qHat
        # if self.winCheck(position, 1) != -1:
        #     qHat = self.winCheck(position, 1) + childState.getVHat()
        # else:
        #     qHat = childState.getVHat()
        
        # Update and store all values
        # self.qHats[action].append(qHat)
        # self.numVisits += 1
        # self.numSamples[action] += 1
        
        # self.updateQBar(action)
        # self.updateVHat()
        # self.updateUCB()
        ""
    
    def tree(self, action, depth, depthBudget, exploreParam):
        # If we already know the result of this position
        # if self.winCheck(position, 1) != -1:
        #     return(self.winCheck(position, 1))
        
        # If we are at the bottom of the tree and must simulate
        # if depth == 0:
        #     self.vHat = self.boardEvaluator()
        #     return(self.boardEvaluator())

        # Otherwise, take the optimal move
        # action = self.getStarvingAction()
        # self.update(action, depth, depthBudget)
        # self.updateUCB()
        ""
        
    def getPositions(self):
        # return(deepcopy(self.position))
        ""
        
    def getStarvingAction(self):
        # viableActions = []
        
        # Select all moves of maximal UCB formula value
        # maxUCB = 0
        # for action in self.actions():
        #     if self.UCBs[actions] > maxUCB:
        #         viableActions = [actions]
        #         maxUCB = self.UCBs[actions]
        #     elif self.UCBs[actions] == maxUCB:
        #         viableActions.append(actions)
        
        # return(random.choice(viableActions))
        ""

    def updateQBar(self, action):
        # Update average qHat
        # self.qHats[action] = (self.qHats[action][0] * (self.numSamples[action] - 1) + self.qHats[action][1])/(self.numSamples[action])
        ""
        
    def updateUCB(self, exploreParam = math.sqrt(2)):
        # Plug in UCB formula for all states
        # for action in self.actions():
        #    if self.numSamples[action] != 0:
        #        self.UCBs[action] = self.qBars[action] + math.sqrt(exploreParam * math.log(self.numVisits, 10)/self.numSamples[action])
        #    else:
        #        self.UCBs[action] = float('inf')
        ""
        
    def getVHat(self):
        # return(self.vHat)
        ""
        
    def updateVHat(self):
        # self.vHat = max(self.qBars)
        ""