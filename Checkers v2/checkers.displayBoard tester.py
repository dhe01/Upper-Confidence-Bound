def displayBoard(position):

    board = [str(i) for i in position]
    
    print("-\t" + "\t-\t".join(board[0:4]).replace("0", "-") + "\n")
    print("\t-\t".join(board[4:8]) .replace("0", "-")+ "\t- \n")
    print("-\t" + "\t-\t".join(board[8:12]).replace("0", "-") + "\n")
    print("\t-\t".join(board[12:16]).replace("0", "-") + "\t- \n")
    print("-\t" + "\t-\t".join(board[16:20]).replace("0","-") + "\n")
    print("\t-\t".join(board[20:24]).replace("0", "-") + "\t- \n")
    print("-\t" + "\t-\t".join(board[24:28]).replace("0", "-") + "\n")
    print("\t-\t".join(board[28:32]).replace("0", "-") + "\t- \n")
