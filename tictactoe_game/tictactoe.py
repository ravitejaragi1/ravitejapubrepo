""" print('Hello World')

programming_languages = "Python" , "Java" ,"GoLang" , "c" 

print(type(programming_languages))


for language  in programming_languages: 
    print(language) """



""" print(game)

count = 0 

for row in game:
    print(count , row)
    count += 1  """

""" l = [1,2,3,4,5]
print(l[4])
print(l[-1])
print(l[2:])

l[1] = 99 

print(l) """

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
       

def game_board(game_map=game, player=0, row=0, column=0, just_display=False) :
    try: 
        global a  ## makes string mutable now as we are referencing global variable
        a = "new string "
        print(a)
        print(id(a))
        print("  a   b  c ")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game): 
            print(count,row) 
        return game_map

    except IndexError as e:
        print("Error: Did you input row and column as 0 1 0r2 ?",e)

    except Exception as e:
        print("Something went very wrong!", e)

    #for item in row :
      #  print(item)

#game_board(game_map=game_board, player=1,row=2, column=1)
play = True 
players = [1,2] 
while play: 
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False 
    game = game_board(game, just_display= True)
    while not game_won:
        current_player = 1
        column_choice = int(input("what column do youi want to play? (0,1,2): "))
        row_choice = int(input("what row do youi want to play? (0,1,2): "))
        game = game_board(game, current_player , row_choice , column_choice)





'''game_board()
x = game_board 
x()

print(a) ## strings are immutable , old value is seen here 
print(id(a))'''

def horizontal_win(current_game):
    for row in game: 
        
        if row.count(row[0]) == len(row) and row[0] !=0:
            print(f"player {row[0]} is the wiiner horizontally")
   
def vertical_win(current_game):
    columns = range(len(game))
    print(columns)
    check = [] 
    for col in columns:
        for row in game: 
            
            check.append(row[col])
    for i in check :
        print(i)
        if check.count(check[0]) == len(check) and check[0] != 0: 
            print(f"player {row[0]} is the winner vertically ")


def diagonal_win(current_game):
    diag = []
    for ix in range(len(game)):
        diag.append(game[ix][ix])
    for row in diag: 
        if diag.count(diag[0]) == len(diag) and diag[0] != 0: 
            print(f"player {row[0]} is the winner (/)")
    
    diags2=[]
    for col,row in enumerate(reversed(range(len(game)))):
        diags2.append(game[row][col])

    for row in diags2:
        if diags2.count(diags2[0]) == len(diags2) and diags2[0] != 0: 
            print(f"player {row[0]} is the winner (\)")



horizontal_win(game)
vertical_win(game)
diagonal_win(game)