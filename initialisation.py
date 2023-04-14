def genere_tableau5x5(grille):
    print(grille)

tableau = [
        [" . ", " . ",  " . ",  " . ", " . "],
        [" . ", " . ",  " . ",  " . ", " . "],
        [" . ", " . ",  " . ",  " . ", " . "],
        [" . ", " . ",  " . ",  " . ", " . "],
        [" . ", " . ",  " . ",  " . ", " . "],
    ]
genere_tableau5x5(tableau)


for line in range(5):
        result = str(line) + "" 
        for column in range(5):

            point = tableau[line][column]
            result = result + point 


        print(result)

#ma solution mais sans les chiffres de colonnes du bas
        
