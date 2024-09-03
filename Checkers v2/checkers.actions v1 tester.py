def actions(position, pawns, kings, epawns, ekings, type):
    
    # Whenever a branch is made, the input will be in the form [piece size (1/2), location of piece moved, piece jumped over, ending location]
    moves = []
    
    flag = True
    
    # Check if a pawn jump can be made
    for location in pawns:
        
        if (location // 4) % 2 == 0:
            
            if location % 4 in [0,1,2]:
                
                if (((location + 5) in epawns) or ((location + 5) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings)))  and (location + 9 < 32):
                    
                    flag = False
                    
                    moves.append([1, location, 5, 9])
                
            if location % 4 in [1,2,3]:
                
                if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings))) and (location + 7 < 32):
                    
                    flag = False
                    
                    moves.append([1, location, 4, 7])

        else:
            
            if location % 4 in [0,1,2]:
                
                if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings))) and (location + 9 < 32):
                    
                    flag = False
                    
                    moves.append([1, location, 4, 9])
                
            if location % 4 in [1,2,3]:
                
                if (((location + 3) in epawns) or ((location + 3) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings))) and (location + 7 < 32):
                    
                    flag = False
                    
                    moves.append([1, location, 3, 7])

    # Check if a king jump can be made
    for location in kings:
            
        if (location // 4) % 2 == 0:
            
            if location % 4 in [0,1,2]:
                
                if (((location + 5) in epawns) or ((location + 5) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings))) and (location + 9 < 32):
                    
                    flag = False
                    
                    moves.append([2, location, 5, 9])
                
                if (((location - 4) in epawns) or ((location - 4) in ekings)) and (not (((location - 9) in epawns) or ((location - 9) in ekings))) and (location - 9 >= 0):
                    
                    flag = False
                    
                    moves.append([2, location, -4, -9])
                
            if location % 4 in [1,2,3]:
                
                if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings))) and (location + 7 < 32):
                    
                    flag = False
                    
                    moves.append([2, location, 4, 7])

                if (((location - 3) in epawns) or ((location - 3) in ekings)) and (not (((location - 7) in epawns) or ((location - 7) in ekings))) and (location - 7 >= 0):
                    
                    flag = False
                    
                    moves.append([2, location, -3, -7])

        else:
            
            if location % 4 in [0,1,2]:
                
                if (((location + 4) in epawns) or ((location + 4) in ekings)) and (not (((location + 9) in epawns) or ((location + 9) in ekings))) and (location + 9 < 32):
                    
                    flag = False
                    
                    moves.append([2, location, 4, 9])
                
                if (((location - 5) in epawns) or ((location - 5) in ekings)) and (not (((location - 9) in epawns) or ((location - 9) in ekings))) and (location - 9 >= 0):
                    
                    flag = False
                    
                    moves.append([2, location, -5, -9])
                
            if location % 4 in [1,2,3]:
                
                if (((location + 3) in epawns) or ((location + 3) in ekings)) and (not (((location + 7) in epawns) or ((location + 7) in ekings))) and (location + 7 < 32):
                    
                    flag = False
                    
                    moves.append([2, location, 3, 7])

                if (((location - 4) in epawns) or ((location - 4) in ekings)) and (not (((location - 7) in epawns) or ((location - 7) in ekings))) and (location - 7 >= 0):
                    
                    flag = False
                    
                    moves.append([2, location, -4, -7])
                    
    return(moves)
