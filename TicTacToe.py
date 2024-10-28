def afficher_plateau(plateau): 
    for ligne in plateau:         # Affiche chaque ligne du plateau
        print(" | ".join(ligne))  # Joint les elements de la ligne avec des "|"
        print("-" * 9)            # Affiche une ligne de separation

def verifier_victoire(plateau):
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != ' ':   # Verifie les lignes, colonnes et diagonales pour une victoire
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != ' ':   # Verifie les colonnes
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != ' ':       # Verifie les diagonales
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != ' ':
        return True
    return False

def plateau_rempli(plateau):
    for ligne in plateau:     # Verifie si toutes les cases du plateau sont remplies
        for cell in ligne:
            if cell == ' ':
                return False  # Une case est encore vide
    return True               # Toutes les cases sont remplies

def ia(plateau, signe): 
    opponent = "X" if signe == "O" else "O"     # Une IA tres simple pour jouer contre le joueur
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                plateau[i][j] = signe           # Tente de jouer
                if verifier_victoire(plateau):
                    return i * 3 + j            # Retourne le mouvement en 1D
                plateau[i][j] = ' '             # Annule le mouvement
    for i in range(3):                          # Si pas de victoire, joue au premier endroit disponible
        for j in range(3):
            if plateau[i][j] == ' ':
                return i * 3 + j
    return -1                                   # Aucun mouvement possible

def play_game():
    plateau = [[' ']*3 for _ in range(3)]                                                              # Initialise le plateau et démarre le jeu
    current_player = "X"
    mode = input("Choisissez le mode (1: JvsJ, 2: JvsIA): ")

    while True:
        afficher_plateau(plateau)
        if mode == "1":                                                                                # Mode Joueur contre Joueur
            ligne, col = map(int, input(f"Joueur {current_player}, choisissez (ligne col): ").split())
            if plateau[ligne][col] == ' ':
                plateau[ligne][col] = current_player
            else:
                print("Case deja prise, reessayez.")
                continue
        else:                                                                                          # Mode Joueur contre IA
            if current_player == "X":
                move = int(input(f"Joueur {current_player}, choisissez (0-8): "))
                if move >= 0 and move < 9:
                    ligne, col = move // 3, move % 3
                    if plateau[ligne][col] == ' ':
                        plateau[ligne][col] = current_player
                    else:
                        print("Case deja prise, reessayez.")
                        continue
            else:
                move = ia(plateau, current_player)
                if move != -1:
                    ligne, col = move // 3, move % 3
                    plateau[ligne][col] = current_player
                    print(f"L'IA a joue en {move}.")

        if verifier_victoire(plateau):
            afficher_plateau(plateau)
            print(f"Felicitations, joueur {current_player} ! Vous avez gagne !")
            break
        if plateau_rempli(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break

        current_player = "O" if current_player == "X" else "X"                                         # Change le joueur

if __name__ == "__main__":   # Demarre le jeu
    play_game()
