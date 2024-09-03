from copy import deepcopy

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
                    
                    moves.append(jump)
                
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
                    
                    newactions = actions(newpawns, newkings, newepawns, newekings, key)
                    
                    for action in newactions:
                        moves.append([jump, action])
        
        # No jumps, so only normal moves
        else:
            
            # Check if a pawn step can be made
            for location in pawns:
                
                if (location // 4) % 2 == 0:
                    
                    if location % 4 in [0,1,2]:
                        
                        if not (((location + 5) in epawns) or ((location + 5) in ekings) or ((location + 5) in pawns) or ((location + 5) in kings)) and (location + 5 < 32):
                                                    
                            moves.append([1, location, 5])
                        
                    if location % 4 in [0,1,2,3]:
                        
                        if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                    
                            moves.append([1, location, 4])

                else:
                    
                    if location % 4 in [0,1,2,3]:
                        
                        if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                    
                            moves.append([1, location, 4])
                        
                    if location % 4 in [1,2,3]:
                        
                        if not (((location + 3) in epawns) or ((location + 3) in ekings) or ((location + 3) in pawns) or ((location + 3) in kings)) and (location + 3 < 32):
                                                    
                            moves.append([1, location, 3])

            # Check if a king step can be made
            for location in kings:
                    
                if (location // 4) % 2 == 0:
                    
                    if location % 4 in [0,1,2]:
                        
                        if not (((location + 5) in epawns) or ((location + 5) in ekings) or ((location + 5) in pawns) or ((location + 5) in kings)) and (location + 5 < 32):
                                                    
                            moves.append([1, location, 5])

                        if not (((location - 3) in epawns) or ((location - 3) in ekings) or ((location - 3) in pawns) or ((location - 3) in kings)) and (location - 3 >= 0):
                                                    
                            moves.append([1, location, -3])
                            
                    if location % 4 in [0,1,2,3]:
                        
                        if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                    
                            moves.append([1, location, 4])
                        
                        if not (((location - 4) in epawns) or ((location - 4) in ekings) or ((location - 4) in pawns) or ((location - 4) in kings)) and (location - 4 >= 0):
                                                    
                            moves.append([1, location, -4])
                            
                else:
                    
                    if location % 4 in [0,1,2,3]:
                        
                        if not (((location + 4) in epawns) or ((location + 4) in ekings) or ((location + 4) in pawns) or ((location + 4) in kings)) and (location + 4 < 32):
                                                    
                            moves.append([1, location, 4])

                        if not (((location - 4) in epawns) or ((location - 4) in ekings) or ((location - 4) in pawns) or ((location - 4) in kings)) and (location - 4 >= 0):
                                                    
                            moves.append([1, location, -4])

                        
                    if location % 4 in [1,2,3]:
                        
                        if not (((location + 3) in epawns) or ((location + 3) in ekings) or ((location + 3) in pawns) or ((location + 3) in kings)) and (location + 3 < 32):
                                                    
                            moves.append([1, location, 3])

                        if not (((location - 5) in epawns) or ((location - 5) in ekings) or ((location - 5) in pawns) or ((location - 5) in kings)) and (location - 5 >= 0):
                                                    
                            moves.append([1, location, -5])

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
                    
                    moves.append(jump)
                
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
                    
                    newactions = actions(newpawns, newkings, newepawns, newekings, key)
                    
                    for action in newactions:
                        moves.append([jump, action])
    
    if len(moves) == 0:
        moves.append([""])
    
    return(moves)
