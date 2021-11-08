'''groups.py
data una lista di x nomi creare y gruppi da z 
partecipanti con ordine casuale
'''
import random
import math


print('''
Se vuoi inserire i nomi dei partecipanti su un file
separato, crea un file denominato "list.txt" ed
inserisci un nome per riga, altrimenti il 
programma chiederà di inserire ogni nome
''')

try:
    input("Premi [INVIO] per coninuare ")
    print("\n\n")

    names = []
    def read_names():
        i = 0
        max = int(input("Numero di partecipanti: "))
        while i < max:
            ok = False
            while not ok:
                n = input(f"Insersci il {i + 1}° nome: ").strip()
                if n:
                    ok = True
                    names.append(n)
                    i += 1

    try:
        f = open("./list.txt", "r")
        lines = f.readlines()

        if(lines):
            print(f'Lettura nomi dal file "list.txt"\nPartecipanti trovati: {len(lines)}\n')
            i = 0
            while i < len(lines):
                names.append(lines[i].replace("\n", "").strip())
                i += 1
        else:
            read_names()
    except FileNotFoundError:
        read_names()
        
    n_par = len(names) # numero partecipanti
    random.shuffle(names)

    n_grp_par = int(input("\nDa quanto devono essere i gruppi? "))
    print('Se dovessero rimanere partecipanti senza gruppo\nverranno distribuiti casualmente tra i gruppi esistenti\n')
    
    n_grp = math.floor(n_par / n_grp_par) # numero gruppi

    n_par_left = n_par % n_grp_par # numero di persone rimanenti
    par_left = [] # persone rimanenti
    for x in range(0, n_par_left):
        par_left.append(names[n_par + x - 2])

    i = 0
    groups = []

    for g in range(0, n_grp):
        groups.append([])
        for p in range(0, n_grp_par):
            groups[g].append(names[p + g*n_grp_par])

    for name in par_left:
        free_groups = [] # indexes of groups which have not reached the limit [n_grp_par + 1]
        for g in groups:
            if len(g) == n_grp_par:
                free_groups.append(groups.index(g)) # adding the index of the free group (index in groups) to free_groups
        i = free_groups[random.randint(0, len(free_groups) - 1)] # select a random free group and grab the index
        groups[i].append(name) # adding name to the random group
    

    # Try to create a groups.txt file 
    # If the script is on a web compiler it can't create the file
    # so we'll skip this
    groups_file = False # Setting to false and then setting to the file instance if it can be created.
    try: 
        groups_file = open("./groups.txt", "w")
        groups_file.write("")
    except PermissionError: pass

    if groups_file:
        L = []
        print('File "groups.txt" creato contenente i gruppi')
        for g in groups:
            L.append(f"Gruppo #{groups.index(g) + 1}\n")
            L.append(" ".join(g) + "\n\n")
        groups_file.writelines(L)
    else:
        print("I gruppi sono:\n")
        for g in groups:
            print(f"Gruppo #{groups.index(g) + 1}")
            print(" ".join(g) + "\n")
        
            

except KeyboardInterrupt:
    print("\n\nProgramma interrotto...\n")

