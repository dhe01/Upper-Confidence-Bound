import math
from array import *
from copy import deepcopy
from functools import partial

class checkers:
    
    # Player pieces are denoted 1 (pawn) and 2 (king), opponents are negative
    def __init__(self, player = 1, position = [1] * 12 + [0] * 8 + [-1] * 12):
        
        if player == 1:
            self.position = position
        else:
            self.position = [-position[31-i] for i in range(32)]
            
        self.pawns = []
        self.kings = []
        self.epawns = []
        self.ekings = []
        
        self.type = "all"
        self.actions = []
        
        self.win = 0
        self.winMove = []
        self.notlMove = []
        self.optimalActions = []
                
    # Find location and count of all pieces
    def updateLocation(self):
        
        pawns = []
        kings = []
        epawns = []
        ekings = []
        
        for index, piece in enumerate(self.position):
            if piece == 1:
                pawns.append(index)
            elif piece == 2:
                kings.append(index)
            elif piece == -1:
                epawns.append(index)
            elif piece == -2:
                ekings.append(index)
        
        self.pawns = pawns
        self.kings = kings
        self.epawns = epawns
        self.ekings = ekings
        
    # Find all possible actions
    def actions(pawns, kings, epawns, ekings, key):
        
        # Whenever a branch is made, the input will be in the form [piece size (1/2), location of piece moved, piece jumped over, ending location]
        jumps = []
        
        # jumps have length 4, regular moves have length 3
        moves = []
        
        if key == None:
            
            # Check if a pawn jump can be made
            for location in pawns:
                
                if (location // 4) % 2 == 0:
                    
                    if location % 4 in [0,1,2]:
                        
                        if (((location + 5) in epawns) or ((location + 5) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings) or ((location + 9) in pawns) or ((location + 9) in kings))) and (location + 9 < 32):
                                                    
                            jumps.append([1, location, 5, 9])
                        
                    if location % 4 in [1,2,3]:
                        
                        if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings) or ((location + 7) in pawns) or ((location + 7) in kings))) and (location + 7 < 32):
                                                    
                            jumps.append([1, location, 4, 7])

                else:
                    
                    if location % 4 in [0,1,2]:
                        
                        if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings)) or ((location + 9) in pawns) or ((location + 9) in kings)) and (location + 9 < 32):
                                                    
                            jumps.append([1, location, 4, 9])
                        
                    if location % 4 in [1,2,3]:
                        
                        if (((location + 3) in epawns) or ((location + 3) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings) or ((location + 7) in pawns) or ((location + 7) in kings))) and (location + 7 < 32):
                                                    
                            jumps.append([1, location, 3, 7])

            # Check if a king jump can be made
            for location in kings:
                    
                if (location // 4) % 2 == 0:
                    
                    if location % 4 in [0,1,2]:
                        
                        if (((location + 5) in epawns) or ((location + 5) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings) or ((location + 9) in pawns) or ((location + 9) in kings))) and (location + 9 < 32):
                                                    
                            jumps.append([2, location, 5, 9])
                        
                        if (((location - 3) in epawns) or ((location - 3) in ekings)) and (not (((location - 7) in epawns) or ((location - 7) in ekings) or ((location - 7) in pawns) or ((location - 7) in kings))) and (location - 7 >= 0):
                                                    
                            jumps.append([2, location, -3, -7])
                        
                    if location % 4 in [1,2,3]:
                        
                        if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings) or ((location + 7) in pawns) or ((location + 7) in kings))) and (location + 7 < 32):
                                                    
                            jumps.append([2, location, 4, 7])

                        if (((location - 4) in epawns) or ((location - 4) in ekings)) and (not (((location - 9) in epawns) or ((location - 9) in ekings) or ((location - 9) in pawns) or ((location - 9) in kings))) and (location - 9 >= 0):
                                                    
                            jumps.append([2, location, -4, -9])
                            
                else:
                    
                    if location % 4 in [0,1,2]:
                        
                        if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings) or ((location + 9) in pawns) or ((location + 9) in kings))) and (location + 9 < 32):
                                                    
                            jumps.append([2, location, 4, 9])

                        if (((location - 4) in epawns) or ((location - 4) in ekings)) and (not (((location - 7) in epawns) or ((location - 7) in ekings) or ((location - 7) in pawns) or ((location - 7) in kings))) and (location - 7 >= 0):
                                                    
                            jumps.append([2, location, -4, -7])
                        
                    if location % 4 in [1,2,3]:
                        
                        if (((location + 3) in epawns) or ((location + 3) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings) or ((location + 7) in pawns) or ((location + 7) in kings))) and (location + 7 < 32):
                                                    
                            jumps.append([2, location, 3, 7])
                            
                        if (((location - 5) in epawns) or ((location - 5) in ekings)) and (not (((location - 9) in epawns) or ((location - 9) in ekings) or ((location - 9) in pawns) or ((location - 9) in kings))) and (location - 9 >= 0):
                                                    
                            jumps.append([2, location, -5, -9])
                            
            # If a jump can be made:
            if len(jumps) > 0:
                
                for jump in jumps:
                    
                    # If the jump promotes the pawn
                    if jump[0] == 1 and (jump[1] + jump[3]) // 4 == 7:
                        
                        moves.append([jump])
                    
                    else:
                        
                        newpawns = deepcopy(pawns)
                        newkings = deepcopy(kings)
                        newepawns = deepcopy(epawns)
                        newekings = deepcopy(ekings)
                        
                        if jump[0] == 1:                            
                            newpawns.remove(jump[1])
                        else:
                            newkings.remove(jump[1])

                        if (jump[1] + jump[2]) in epawns:
                            newepawns.remove(jump[1] + jump[2])
                        
                        else:
                            newekings.remove(jump[1] + jump[2])
                                
                        if jump[0] == 1:
                            newpawns.append(jump[1] + jump[3])
                        else:
                            newkings.append(jump[1] + jump[3])
                        
                        key = jump[1] + jump[3]
                        
                        newactions = checkers.actions(newpawns, newkings, newepawns, newekings, key)
                        
                        moves += [[jump] + [action] for action in newactions[0]]
            
            # No jumps, so only normal moves
            else:
                
                # Check if a pawn step can be made
                for location in pawns:
                    
                    if (location // 4) % 2 == 0:
                        
                        if location % 4 in [0,1,2]:
                            
                            if not (((location + 5) in epawns) or ((location + 5) in ekings) or ((location + 5) in pawns) or ((location + 5) in kings)) and (location + 5 < 32):
                                                        
                                moves.append([[1, location, 5]])
                            
                        if location % 4 in [0,1,2,3]:
                            
                            if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                        
                                moves.append([[1, location, 4]])

                    else:
                        
                        if location % 4 in [0,1,2,3]:
                            
                            if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                        
                                moves.append([[1, location, 4]])
                            
                        if location % 4 in [1,2,3]:
                            
                            if not (((location + 3) in epawns) or ((location + 3) in ekings) or ((location + 3) in pawns) or ((location + 3) in kings)) and (location + 3 < 32):
                                                        
                                moves.append([[1, location, 3]])

                # Check if a king step can be made
                for location in kings:
                        
                    if (location // 4) % 2 == 0:
                        
                        if location % 4 in [0,1,2]:
                            
                            if not (((location + 5) in epawns) or ((location + 5) in ekings) or ((location + 5) in pawns) or ((location + 5) in kings)) and (location + 5 < 32):
                                                        
                                moves.append([[2, location, 5]])

                            if not (((location - 3) in epawns) or ((location - 3) in ekings) or ((location - 3) in pawns) or ((location - 3) in kings)) and (location - 3 >= 0):
                                                        
                                moves.append([[2, location, -3]])
                                
                        if location % 4 in [0,1,2,3]:
                            
                            if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                        
                                moves.append([[2, location, 4]])
                            
                            if not (((location - 4) in epawns) or ((location - 4) in ekings) or ((location - 4) in pawns) or ((location - 4) in kings)) and (location - 4 >= 0):
                                                        
                                moves.append([[2, location, -4]])
                                
                    else:
                        
                        if location % 4 in [0,1,2,3]:
                            
                            if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                        
                                moves.append([[2, location, 4]])

                            if not (((location - 4) in epawns) or ((location - 4) in ekings) or ((location - 4) in pawns) or ((location - 4) in kings)) and (location - 4 >= 0):
                                                        
                                moves.append([[2, location, -4]])

                            
                        if location % 4 in [1,2,3]:
                            
                            if not (((location + 3) in epawns) or ((location + 3) in ekings) or ((location + 3) in pawns) or ((location + 3) in kings)) and (location + 3 < 32):
                                                        
                                moves.append([[2, location, 3]])

                            if not (((location - 5) in epawns) or ((location - 5) in ekings) or ((location - 5) in pawns) or ((location - 5) in kings)) and (location - 5 >= 0):
                                                        
                                moves.append([[2, location, -5]])

        # There was a previous jump
        else:
            
            if key in pawns:
                                
                if (key // 4) % 2 == 0:
                    
                    if key % 4 in [0,1,2]:
                        
                        if (((key + 5) in epawns) or ((key + 5) in ekings)) and (not (((key + 9) in epawns) or ((key + 9) in ekings) or ((key + 9) in pawns) or ((key + 9) in kings))) and (key + 9 < 32):
                                                    
                            jumps.append([1, key, 5, 9])
                        
                    if key % 4 in [1,2,3]:
                        
                        if (((key + 4) in epawns) or ((key + 4) in ekings)) and (not (((key + 7) in epawns) or ((key + 7) in ekings) or ((key + 7) in pawns) or ((key + 7) in kings))) and (key + 7 < 32):
                                                    
                            jumps.append([1, key, 4, 7])

                else:
                    
                    if key % 4 in [0,1,2]:
                        
                        if (((key + 4) in epawns) or ((key + 4) in ekings)) and (not (((key + 9) in epawns) or ((key + 9) in ekings) or ((key + 9) in pawns) or ((key + 9) in kings))) and (key + 9 < 32):
                                                    
                            jumps.append([1, key, 4, 9])
                        
                    if key % 4 in [1,2,3]:
                        
                        if (((key + 3) in epawns) or ((key + 3) in ekings)) and (not (((key + 7) in epawns) or ((key + 7) in ekings) or ((key + 7) in pawns) or ((key + 7) in kings))) and (key + 7 < 32):
                                                    
                            jumps.append([1, key, 3, 7])

            # Check if a king jump can be made
            if key in kings:
                    
                if (key // 4) % 2 == 0:
                    
                    if key % 4 in [0,1,2]:
                        
                        if (((key + 5) in epawns) or ((key + 5) in ekings)) and (not (((key + 9) in epawns) or ((key + 9) in ekings) or ((key + 9) in pawns) or ((key + 9) in kings))) and (key + 9 < 32):
                                                    
                            jumps.append([2, key, 5, 9])
                        
                        if (((key - 3) in epawns) or ((key - 3) in ekings)) and (not (((key - 7) in epawns) or ((key - 7) in ekings) or ((key - 7) in pawns) or ((key - 7) in kings))) and (key - 7 >= 0):
                                                    
                            jumps.append([2, key, -3, -7])
                        
                    if key % 4 in [1,2,3]:
                        
                        if (((key + 4) in epawns) or ((key + 4) in ekings)) and (not (((key + 7) in epawns) or ((key + 7) in ekings) or ((key + 7) in pawns) or ((key + 7) in kings))) and (key + 7 < 32):
                                                    
                            jumps.append([2, key, 4, 7])
                        
                        if (((key - 4) in epawns) or ((key - 4) in ekings)) and (not (((key - 9) in epawns) or ((key - 9) in ekings) or ((key - 9) in pawns) or ((key - 9) in kings))) and (key - 9 >= 0):
                                                    
                            jumps.append([2, key, -4, -9])
                            
                else:
                    
                    if key % 4 in [0,1,2]:
                        
                        if (((key + 4) in epawns) or ((key + 4) in ekings)) and (not (((key + 9) in epawns) or ((key + 9) in ekings) or ((key + 9) in pawns) or ((key + 9) in kings))) and (key + 9 < 32):
                                                    
                            jumps.append([2, key, 4, 9])
                        
                        if (((key - 4) in epawns) or ((key - 4) in ekings)) and (not (((key - 7) in epawns) or ((key - 7) in ekings) or ((key - 7) in pawns) or ((key - 7) in kings))) and (key - 7 >= 0):
                                                    
                            jumps.append([2, key, -4, -7])
                        
                    if key % 4 in [1,2,3]:
                        
                        if (((key + 3) in epawns) or ((key + 3) in ekings)) and (not (((key + 7) in epawns) or ((key + 7) in ekings) or ((key + 7) in pawns) or ((key + 7) in kings))) and (key + 7 < 32):
                                                    
                            jumps.append([2, key, 3, 7])

                        if (((key - 5) in epawns) or ((key - 5) in ekings)) and (not (((key - 9) in epawns) or ((key - 9) in ekings) or ((key - 9) in pawns) or ((key - 9) in kings))) and (key - 9 >= 0):
                                                    
                            jumps.append([2, key, -5, -9])
                                         
            if len(jumps) > 0:
                
                for jump in jumps:
                    
                    # If the jump promotes the pawn
                    if jump[0] == 1 and (jump[1] + jump[3]) // 4 == 7:
                        
                        moves.append([jump])
                    
                    else:
                        
                        newpawns = deepcopy(pawns)
                        newkings = deepcopy(kings)
                        newepawns = deepcopy(epawns)
                        newekings = deepcopy(ekings)
                        
                        if jump[0] == 1:                            
                            newpawns.remove(jump[1])
                        else:
                            newkings.remove(jump[1])

                        if (jump[1] + jump[2]) in epawns:
                            newepawns.remove(jump[1] + jump[2])
                        
                        else:
                            newekings.remove(jump[1] + jump[2])
                                
                        if jump[0] == 1:
                            newpawns.append(jump[1] + jump[3])
                        else:
                            newkings.append(jump[1] + jump[3])
                        
                        key = jump[1] + jump[3]
                        
                        newactions = checkers.actions(newpawns, newkings, newepawns, newekings, key)
                        
                        moves += [[jump] + [action] for action in newactions[0]]
        
        if len(moves) == 0:
            moves = [[[""]]]
        
        return(moves)

    # Update actions with actions()
    def updateActions(self):
        self.updateLocation()
        self.actions = checkers.actions(self.pawns, self.kings, self.epawns, self.ekings, None)
    
    def opponentAction(self):
        
        fpawns = [31-i for i in self.epawns]
        fkings = [31-i for i in self.ekings]
        fepawns = [31-i for i in self.pawns]
        fekings = [31-i for i in self.kings]
        
        fposition = []
        for index in range(32):
            if index in fpawns:
                fposition.append(1)
            elif index in fkings:
                fposition.append(2)
            elif index in fepawns:
                fposition.append(-1)
            elif index in fekings:
                fposition.append(-2)
            else:
                fposition.append(0)
        
        fsubposition = checkers(position = fposition)
        return(fsubposition.optimalActions)
    
    # REDUNDANT TO flip()??? MIGHT DELETE
    def opponentAction(pawns, kings, epawns, ekings):
        
        fpawns = [31-i for i in epawns]
        fkings = [31-i for i in ekings]
        fepawns = [31-i for i in pawns]
        fekings = [31-i for i in kings]
        
        fposition = []
        for index in range(32):
            if index in fpawns:
                fposition.append(1)
            elif index in fkings:
                fposition.append(2)
            elif index in fepawns:
                fposition.append(-1)
            elif index in fekings:
                fposition.append(-2)
            else:
                fposition.append(0)
        
        fsubposition = checkers(position = fposition)
        return(fsubposition.optimalActions)
        
    # Update board position after an action
    def updateBoard(self, action):
        
        print(action)
        
        self.updateActions()
        
        pawns = deepcopy(self.pawns)
        kings = deepcopy(self.kings)
        epawns = deepcopy(self.epawns)
        ekings = deepcopy(self.ekings)
        
        print()
        #print(pawns)
        #print(kings)
        #print(epawns)
        #print(ekings)
        #print()
        
        position = []
        for index in range(32):
            if index in pawns:
                position.append(1)
            elif index in kings:
                position.append(2)
            elif index in epawns:
                position.append(-1)
            elif index in ekings:
                position.append(-2)
            else:
                position.append(0)
        
        subposition = checkers(position = position)
        subposition.updateLocation()
        #print(subposition.moves)
        
        for step in action:
            
            #print(step)
            
            if step == [""]:
                
                break
            
            elif len(step) == 3:
                
                if step[0] == 1:

                    pawns.remove(step[1])
                    
                    if (step[1] + step[2]) // 4 == 7:
                        kings.append(step[1] + step[2])
                        
                    else:
                        pawns.append(step[1] + step[2])
                    
                else:
                    
                    kings.remove(step[1])
                    kings.append(step[1] + step[2])
                
            else:
                
                if step[0] == 1:
                    
                    pawns.remove(step[1])
                    
                    if (step[1] + step[2]) in epawns:
                        epawns.remove(step[1] + step[2])
                    else:
                        ekings.remove(step[1] + step[2])
                    
                    if (step[1] + step[3]) // 4 == 7:
                        kings.append(step[1] + step[3])
                    else:
                        pawns.append(step[1] + step[3])

                else:
                                        
                    kings.remove(step[1])

                    if (step[1] + step[2]) in epawns:
                        epawns.remove(step[1] + step[2])
                    else:
                        ekings.remove(step[1] + step[2])
                        
                    kings.append(step[1] + step[3])
                
        board = []
        for space in range(31):
            if space in pawns:
                board.append(1)
            elif space in kings:
                board.append(2)
            elif space in epawns:
                board.append(-1)
            elif space in ekings:
                board.append(-2)
            else:
                board.append(0)
        
        self.position = board
        self.pawns = pawns
        self.kings = kings
        self.epawns = epawns
        self.ekings = ekings

    # Print out the board
    def displayBoard(self):
        
        board = [str(i) for i in deepcopy(self.position)]
        
        print("-\t" + "\t-\t".join(board[0:4]).replace("0", "-") + "\n")
        print("\t-\t".join(board[4:8]) .replace("0", "-")+ "\t- \n")
        print("-\t" + "\t-\t".join(board[8:12]).replace("0", "-") + "\n")
        print("\t-\t".join(board[12:16]).replace("0", "-") + "\t- \n")
        print("-\t" + "\t-\t".join(board[16:20]).replace("0","-") + "\n")
        print("\t-\t".join(board[20:24]).replace("0", "-") + "\t- \n")
        print("-\t" + "\t-\t".join(board[24:28]).replace("0", "-") + "\n")
        print("\t-\t".join(board[28:32]).replace("0", "-") + "\t- \n")
    
    # See if the game is won
    def winCheck(pawns, kings, epawns, ekings):

        if len(epawns) + len(ekings) == 0:
            return(True)
        
        # Flipping the board and seeing if there are any enemy moves (if no moves possible, game is won)
        fpawns = [31-i for i in epawns]
        fkings = [31-i for i in ekings]
        fepawns = [31-i for i in pawns]
        fekings = [31-i for i in kings]
        
        if [''] in checkers.actions(fpawns, fkings, fepawns, fekings, None):
            return(True)
        
        return(False)
    
    def winUpdate(self):
        
        if checkers.winCheck(self.pawns, self.kings, self.epawns, self.ekings):

            self.win = 1
            return(True)

        return(False)
    
    def winningMove(self):
        
        for action in self.actions:
            
            print("winning move")
            print(action)
            
            subposition = checkers(position = self.position)
            subposition.updateBoard(action = action)
            if subposition.winUpdate():
                self.winMove = action
                self.win = 1
                return(action)
        
        self.winMove = [[""]]
        return([[""]])
        
    def blockWinningMove(self):
        
        validActions = []
        
        for action in self.actions:
            
            subposition = checkers(position = self.position)
            subposition.updateBoard(action = action)
            
            fpawns = [31-i for i in subposition.epawns]
            fkings = [31-i for i in subposition.ekings]
            fepawns = [31-i for i in subposition.pawns]
            fekings = [31-i for i in subposition.kings]
            
            subposition.pawns = fpawns
            subposition.kings = fkings
            subposition.epawns = fepawns
            subposition.ekings = fekings
            
            fposition = []
            for index in range(32):
                if index in fpawns:
                    fposition.append(1)
                elif index in fkings:
                    fposition.append(2)
                elif index in fepawns:
                    fposition.append(-1)
                elif index in fekings:
                    fposition.append(-2)
                else:
                    fposition.append(0)
            
            fsubposition = checkers(position = fposition)
            
            if [""] in fsubposition.winningMove():
                validActions.append(action)
        
        if len(validActions) == 0:
            validActions = [[""]]
            
        self.notlMove = validActions
        return(validActions)
    
    def flip(pawns, kings, epawns, ekings):
        
        fpawns = [31-i for i in epawns]
        fkings = [31-i for i in ekings]
        fepawns = [31-i for i in pawns]
        fekings = [31-i for i in kings]
        
        fposition = []
        for index in range(32):
            if index in fpawns:
                fposition.append(1)
            elif index in fkings:
                fposition.append(2)
            elif index in fepawns:
                fposition.append(-1)
            elif index in fekings:
                fposition.append(-2)
            else:
                fposition.append(0)
        
        fsubposition = checkers(position = fposition)
        return(fsubposition)

    def updateAll(self):
        self.updateActions()
        # print(self.actions)
        
        self.winUpdate()
        self.winningMove()
        self.blockWinningMove()
        
        if self.winMove == [[""]]:
            self.optimalActions = self.notlMove
        else:
            self.optimalActions = self.winMove
