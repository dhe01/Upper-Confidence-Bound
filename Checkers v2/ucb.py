import random
import math
from array import *
from copy import deepcopy
import numpy as np
from checkers import checkers

class ucb:
    
    def __init__(self, position = [1] * 12 + [0] * 8 + [-1] * 12, explore_param = math.sqrt(2), depth = 5):
        
        self.checkers = checkers(position = position)
        self.checkers.updateAll()
        
        self.children = {}
        
        self.position = []
        self.explore_param = explore_param
        
        self.total_visits = 0
        self.num_visits = {}
        self.depth = 5
        
        self.UCBVals = {}
        self.qBar = {}
        self.qHat = 0
        
        self.vHat = []
        self.optimalActions = []
                        
    def opponentAction(pawns, kings, epawns, ekings):
        
        flipState = checkers.flip(pawns, kings, epawns, ekings)
        flipState.updateAll()
        return(random.choice(flipState.optimalActions))
    
    # todo: Move tuplefy out of ucb
    def tuplefy(move):
        
        newmove = []
        
        for step in move:
            
            newmove.append(tuple(step))
            
        return(tuple(newmove))
    
    def update(self, move, depth):

        if self.checkers.win == 1:
            return(1)
                
        position = deepcopy(self.checkers)
        position.updateBoard(move)

        opponentMove = ucb.opponentAction(position.pawns, position.kings, position.epawns, position.ekings)
        opponentBoard = checkers.flip(position.pawns, position.kings, position.epawns, position.ekings)
        opponentBoard.updateBoard(opponentMove)
        subposition = checkers.flip(opponentBoard.pawns, opponentBoard.kings, opponentBoard.epawns, opponentBoard.ekings)
        subposition.updateAll

        if depth > 1:
                    
            if ucb.tuplefy(move) in self.children:
                
                childState = self.children[ucb.tuplefy(move)]
                childState.position = subposition.position
            
            else:
            
                childState = ucb(position = subposition.position, explore_param = self.explore_param, depth = self.depth)
                self.children[ucb.tuplefy(move)] = childState
            
            self.total_visits += 1
            
            childMove = childState.starvingAction()
            qval = childState.update(childMove, depth - 1)
            
            if ucb.tuplefy(move)in self.UCBVals:
                self.qBar[ucb.tuplefy(move)] = (self.qBar[ucb.tuplefy(move)] * self.num_visits[ucb.tuplefy(move)] + qval)/(self.num_visits[ucb.tuplefy(move)])
                self.num_visits[ucb.tuplefy(move)] += 1
                self.UCBVals[ucb.tuplefy(move)] = self.qBar[ucb.tuplefy(move)] + self.explore_param * math.sqrt(math.log(self.total_visits)/self.num_visits[ucb.tuplefy(move)])
                
            else:
                self.qBar[ucb.tuplefy(move)] = qval
                self.num_visits[ucb.tuplefy(move)] = 1
                self.UCBVals[ucb.tuplefy(move)] = self.qBar[ucb.tuplefy(move)] + self.explore_param * math.sqrt(math.log(self.total_visits))

            for i in self.qBar:
                if self.qBar[i] > self.qHat:
                    self.qHat = self.qBar[i]
                    
            return(self.qHat)
        
        else:
            
            return(ucb.rollout(subposition))
            
    def rollout(position):
        
        board = checkers(position)
        
        for iter in range(40):
                
            board.updateAll()
            if board.win == 1:
                return(1)
    
            board.updateBoard(random.choice(board.optimalActions))
            board = checkers.flip(board.pawns, board.kings, board.epawns, board.ekings)
            board.updateAll()
            if board.win == 1:
                return(-1)    
            board.updateBoard(random.choice(board.optimalActions))
            board = checkers.flip(board.pawns, board.kings, board.epawns, board.ekings)
        
        board.updateLocation()
        return((len(board.pawns) + 1.5 * len(board.kings))/(len(board.pawns) + len(board.epawns) + 1.5 * len(board.kings) + 1.5 * len(board.ekings)))
    
    def starvingAction(self):
        
        maxUCB = 0
        maxAction = []
        
        for action in self.checkers.actions:
            
            if not (ucb.tuplefy(action) in self.children):
                
                return(action)

            if self.UCBVals[ucb.tuplefy(action)] > maxUCB:
                
                maxUCB = self.UCBVals[ucb.tuplefy(action)] 
                maxAction = action
        
        return(maxAction)
    
    def simulate(self):
        
        if self.checkers.win == 1:
            
            return(self.checkers.optimalActions)
        
        for val in range(5):
            
            self.update(self.starvingAction(), self.depth)
        
        for i in self.qBar:
            if self.qBar[i] == self.qHat:
                return(i)
