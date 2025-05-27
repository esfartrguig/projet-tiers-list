# liste_nom_tmp1 = "Noah, Basmala, Mohammed, Elyas"
# liste_nom_tmp2 = ["Noah", "Basmala", "Mohammed", "Elyas"]

list_users = []

user_01 = ["Wayne", "Bruce", "notbatman@gmail.com"]
user_02 = ["Parker", "Peter", "spidey@gmail.com"]
user_03 = ["Kent", "Clark", "unmecnormal@gmail.com"]

list_users.append(user_01)
list_users.append(user_02)
list_users.append(user_03)

with open("09_liste_noms.txt", "w") as file:
    n = 0
    for user in list_users:      
        m = 0
        if n != 0:
            file.write("\n")
        n += 1
        for data in user:
            length_user = len(user) - 1
            if m != length_user:
                file.write(f"{data}, ")
            else:
                file.write(f"{data}")
            m += 1

with open("09_liste_noms.txt", "r") as file:
    liste_nom = file.read()
    print(liste_nom)
