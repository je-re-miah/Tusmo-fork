
def lettre_correcte(mot, place, solution):
    """Teste si la lettre du mot rentré par l'utilisateur se
    trouve dans le mot-solution et si elle est bien placée

    Paramètres
    ----------
    mot : string
        le mot entré par l'utilisateur
    place : int
        le rang de la lettre dans le mot
    solution : string
        le mot-solution à trouver

    Retourne
    --------
    Le statut de la lettre : int
        0 si absente, 1 si mal placée, 2 si bien placée
    """
    if mot[place] not in solution:
        # la lettre n'est pas dans le mot-solution
        return 0
    else:
        # la lettre est dans le mot-solution
        if mot[place] == solution[place]:
            # la lettre est bien placée
            return 2
        else:
            # la lettre est mal placée
            return 1


def mot_correct(mot, solution):
    """Teste si le mot entré par l'utilisateur est correct

    Paramètres
    ----------
    mot : string
        le mot rentré par l'utilisateur
    solution : string
        le mot correct

    Retourne
    --------
    True si l'utilisateur trouve le bon mot
    False si l'utilisateur n'as pas trouvé le mot
    """
    global nb
    cnt_correct = 0     # le nombre de lettres bien placées
    for i in range(len(mot)):
        lettre = lettre_correcte(mot, i, solution)
        print(mot[i], ":", lettre)
        if lettre == 2:
            cnt_correct += 1
        nb.append(lettre)
    print(nb)    return cnt_correct == len(mot)   

def diff4(solution,guess,t):
    for i in range(len(solution)):
        lettre = solution[i]
        for j in range(len(guess)):
            if guess[j] == guess[i]:
                if guess[j] == lettre:
                    t[i] = 2
                    pass
    return t

def diff_check(guess,solution,t):
    good = True
    for i in range(len(t)):
        if t[i] == 2:
            if guess[i] != solution[i]:
                good = False
    return good
