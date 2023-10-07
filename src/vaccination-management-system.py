import json
import random


def callList(name):
    try:
        f = open(f"{name}.txt", "r")
        y = json.load(f)
        for i in range(0, y.__len__()):
            if y[i] == [1, 1, 1, 1, 1, 1]:
                y.pop(i)
        f.close
        return y
    except:
        y = [[1, 1, 1, 1, 1, 1]]
        writeList(name, y)
        return y


def writeList(name, list):
    f = open(f"{name}.txt", "w")
    json.dump(list, f)
    f.close


def add(listNeeded, listAdded):
    for index in listNeeded:
        listAdded.append(str(input(index)))
    return listAdded


def checkLogin(i, uData, u, qList):
    for num in range(0, 3):
        if i[num] == uData[num]:
            u += 1
        else:
            print(f"your {qList[num]} is wrong")
            c = str(input("press 1 for reenter your data and 2 for register: "))
            if c == "1":
                login()
            elif c == "2":
                register()
            else:
                print("your input is wrong")
                exit()
    return u


def login():
    list = callList("regestData")
    u = 0
    global specList
    uData = []
    list2 = ["please enter your UserName: ", "please enter your Password: "]
    list3 = [1, "UserName", "password"]

    if list == []:
        if (
            str(input("you dont have any data. if you want create new one press 1: "))
            == "1"
        ):
            register()
        else:
            print("wrong input")
            exit()
    else:
        uData = add(list2, uData)
        for i in list:
            print(uData[0])
            print(i[1])
            if uData[0] == i[1]:
                uData.insert(0, i[0])
                u = checkLogin(i, uData, u, list3)
        if u > 2:
            print(f"hi {uData[1]}")
            for item in range(0, len(list)):
                if list[item][1] == uData[1]:
                    specList = list[item]
        elif u == 0:
            print(f"your user UserName is wrong")
            c = str(input("press 1 for reenter your data and 2 for register: "))
            if c == "1":
                login()
            elif c == "2":
                register()
            else:
                print("your input is wrong")
                exit()


def checkRepeted(index, text, x, y):
    for i in y:
        if i == x[index]:
            z = str(input(f"{text} repeted please re inter it: "))
            x[index] = z
            checkRepeted(index, text, x, y)
    return x


def register():
    id = []
    name = []
    x = []
    global specList
    list = callList("regestData")
    for index in list:
        id.append(index[1])
    for index in list:
        if index[0] == False:
            name.append(index[2])
    u = str(input("press 1 if are you an admin and 2 if you are a patient: "))
    list2 = [
        "please enter your UserName: ",
        "please enter your password: ",
        "please enter your email: ",
    ]
    list3 = ["please enter your phone number: ", "please enter your national id: "]
    if u == "1":
        x = add(list2, x)
        x.insert(0, True)
        x.insert(3, random.random())
        x = checkRepeted(1, "your UserName is", x, name)
        list.insert(0, x)
        specList = x
        print(f"hi {x[2]}")
        writeList("regestData", list)
    elif u == "2":
        x = add(list2, x)
        x.insert(0, False)
        x.insert(3, random.random())
        x = checkRepeted(1, "your UserName is", x, name)
        x = add(list3, x)
        x.insert(10, 0)
        list.insert(0, x)
        specList = x
        print(f"hi {x[1]}")
        writeList("regestData", list)
    else:
        if str(input("wrong input. press 1 for re register: ")) == "1":
            register()
        else:
            print("wrong input")
            quit()


def fopen():
    x = input(
        "********** Login System **********\n0.Exit\n1.Login\n2.Signup\nEnter your choice: "
    )
    if x == "1":
        login()
    elif x == "2":
        register()
    elif x == "0":
        exit()
    else:
        print("the input is wrong")
        fopen()

    if specList[0]:
        admin()
    else:
        user(specList)
    BackUp()


def admin():
    BackUp()
    x = input(
        "\nyou are now in control panel\npress 1 for add center\npress 2 for remove center\npress 3 for search center\npress 4 for List registered users on the system and if they have reservation for a vaccine or not\npress 5 for the all users\npress 6 for see the vaccine requsets\nor any thing else for exit the admin page\nenter your choise: "
    )
    if x == "1":
        addCenter()
        admin()
    elif x == "2":
        removeCenter()
        admin()
    elif x == "3":
        searchCenter()
        admin()
    elif x == "4":
        listUsers()
        admin()
    elif x == "5":
        showUsers()
        admin()
    elif x == "6":
        AcceptReservation()
        admin()
    else:
        print("\nthank you")


def addCenter():
    print("please enter the Vaccination center data:")
    list2 = ["id: ", "name: ", "address: "]
    x = []
    callList("Vaccination centers")
    list = callList("Vaccination centers")
    centerName = []
    for index in list:
        centerName.append(index[1])
    id = []
    for index in list:
        id.append(index[0])
    x = add(list2, x)
    x = checkRepeted(0, "the id is", x, id)
    x = checkRepeted(1, "the name is", x, centerName)
    u = str(input("list of vaccines (space-seprated): "))
    list3 = u.split()
    x.append(list3)
    list.insert(0, x)
    writeList("Vaccination centers", list)


def removeCenter():
    list = callList("Vaccination centers")
    centerName = []
    p = 0
    if list == []:
        if (
            str(input("you dont have any data. if you want create new one press 1: "))
            == "1"
        ):
            addCenter()
        else:
            print("wrong input")
    else:
        print("the list of centers:")
        for index in list:
            if index[1] != 1:
                centerName.append(index[1])
                print(index[1])
        x = str(input("enter the name of the center that you want to delete it: "))
        for i in range(0, len(centerName)):
            if centerName[i].upper() == x.upper():
                del centerName[i]
                del list[i]
                break
            p += 1
        writeList("Vaccination centers", list)
        if p == len(centerName):
            p = str(input("wrong input. If you want to redo the process, press 1: "))
            if p == "1":
                removeCenter()
            else:
                print("wrong input")


def searchCenter():
    list = callList("Vaccination centers")
    x = 0
    if list == []:
        if (
            str(input("you dont have any data. if you want create new one press 1: "))
            == "1"
        ):
            addCenter()
        else:
            print("wrong input")
    else:
        u = str(input("enter the name of the Vaccination center: "))
        for index in list:
            if index[1] != 1:
                if index[1].upper() == u.upper():
                    print(
                        f"id: {index[0]} name: {index[1]} address: {index[2]} list of vaccines:{index[3]}"
                    )
                    x = 1
        if x != 1:
            u = str(
                input(
                    "the name of the Vaccination center that you enter doesn't exist.\npress 1 if you want found another one: "
                )
            )
            if u == "1":
                searchCenter()


def listUsers():
    list = callList("regestData")
    x = []
    users = []
    z = 0
    for index in list:
        if index[0] == False:
            if index[7] != 1 and index[7] != 2:
                x.append(index[1])
                users.append(index)
    u = len(list)
    for i in range(0, len(users)):
        for j in range(0, u):
            if list[j] == users[i]:
                del list[j]
                u -= 1
                break
    if x != []:
        print(
            "Press 1 next to the name if he have reservation for a vaccine and 2 if he don't: "
        )
        for item in range(0, len(users)):
            t = str(input(f"{x[item]}: "))
            if t == "1":
                users[item][7] = 1
            elif t == "2":
                users[item][7] = 2
            else:
                print(
                    f"wrong input. {x[item]} didn't List for if they have reservation for a vaccine or not"
                )
                z += 1
    else:
        print("there is no users yet")
    for item2 in users:
        list.append(item2)
    writeList("regestData", list)
    if z > 0:
        k = str(
            input(
                "there are users didn't List for if they have reservation for a vaccine or not.\npress 1 if you want to edit that: "
            )
        )
        if k == "1":
            listUsers()
        else:
            print("wrong input")


def showUsers():
    list = callList("regestData")
    list2 = callList("vaccine requsets")
    u = 1
    for index in list:
        if index[0] == False:
            if index[7] == 0:
                x = "not rgistert yet by the admins"
            elif index[7] == 1:
                x = "can reservation for a vaccine"
            else:
                x = "cann't reservation for a vaccine"
            print(
                f"{u}.user name: {index[1]} id: {int(index[3] * 1000)} email: {index[4]} phone numper: {index[5]}\nnational id: {index[6]}, {x}."
            )
            u += 1
            if index[7] == 1:
                i = 1
                for item in list2:
                    if item[0] == index[1]:
                        if item[3] == 0:
                            print(
                                f"\t{i}.the admins didn't accept {index[2]}'s requset yet for {item[2]} vaccine"
                            )
                            i += 1
                        elif item[3] == "1":
                            print(
                                f"\t{i}.the admins refuse {index[2]}'s requset for {item[2]} vaccine"
                            )
                            i += 1
                        else:
                            print(
                                f"\t{i}.the admins accept {index[2]}'s requset for {item[2]} vaccine and the Schedule your vaccination on the day {item[3]}"
                            )
                            i += 1


def user(speclist):
    BackUp()
    u = 1
    if speclist[7] == 1:
        list = callList("Vaccination centers")
        if list == []:
            print("there is no Vaccination centers aded until now")
            print("check soon if there is one aded")
            return
        else:
            print("\nwelcome in Vaccination scheduling System")
            print("the list of the Vaccination centers:\n")
            for index in list:
                if index[0] != 1:
                    print(
                        f"{u}: id: {index[0]} name: {index[1]} address: {index[2]} list of vaccines:{index[3]}"
                    )
                    u += 1
            x = str(
                input(
                    "\npress 1 to reserve a vaccine\npress 2 to check your vaccination request\nor any thing else for exit the user page\nenter your choise: "
                )
            )
            if x == "1":
                reserveVaccine([0, 0, 0, 0], speclist)
                user(speclist)
            elif x == "2":
                checkrequest(specList)
                user(speclist)
            else:
                print("thank you")
    elif speclist[7] == 2:
        print("the admin rgister you that you can't reservation for a vaccine")
        print("we are soory good luck next time")
        return
    else:
        print(
            "the admin didn't rgister you if you can reservation for a vaccine or not"
        )
        print("you can return soon and check if the amin rgister you")
        return


def reserveVaccine(x, specList):
    list = callList("Vaccination centers")
    x[0] = specList[1]
    z = t = 0
    # global listVaccines
    u = str(input("enter the name of the Vaccination center: "))
    for index in list:
        if index[1] != 1:
            if index[1].upper() == u.upper():
                x[1] = index[0]
                listVaccines = index[3]
                z = 1
    if z != 1:
        u = str(
            input(
                "the name of the Vaccination center that you enter doesn't exist.\npress 1 for enter another one: "
            )
        )
        if u == "1":
            reserveVaccine(x, specList)
        else:
            return
    print(f"the list of vaccines: {listVaccines}")
    u = str(input("enter the name of the vaccine: "))
    for item in listVaccines:
        if item.upper() == u.upper():
            x[2] = item
            t = 1
    if t != 1:
        u = str(
            input(
                "the name of the vaccine that you enter doesn't exist in the Vaccination center.\npress 1 for enter another one: "
            )
        )
        if u == "1":
            reserveVaccine(x, specList)
    list2 = callList("vaccine requsets")
    for item2 in list2:
        if item2[0] == x[0]:
            if item2[1] == x[1]:
                if item2[2] == x[2]:
                    print("you send this requset before")
                    return

    if x[2] != 0:
        print(
            "your requset sent for the admins. check in another time to see if they accept it"
        )
        list2.append(x)
        writeList("vaccine requsets", list2)
    else:
        writeList("vaccine requsets", list2)


def AcceptReservation():
    v = h = 0
    list = callList("vaccine requsets")
    for item in range(0, len(list)):
        if list[item][0] != 1:
            if list[item][3] == 0:
                v += 1
    if list == [[1, 1, 1, 1, 1, 1]] or v == 0:
        print("there is no vaccine requsets now")
    else:
        print(
            "press 1 next to the request if you accept it, 2 for refuse it or any thing else if not:"
        )
        for item in range(0, len(list)):
            if list[item][0] != 1:
                if list[item][3] == 0:
                    print(
                        f"the user {list[item][0]} whants to have {list[item][2]} vaccine in center that have {list[item][1]} as id :"
                    )
                    u = str(input())
                    if u == "1":
                        list[item][3] = str(
                            input(
                                "please enter the date that the user can take the vaccine in(in form dd-mm): "
                            )
                        )
                    elif u == "2":
                        list[item][3] = "1"
                    else:
                        print(
                            f"wrong input. {list[item][0]}'s request didn't List if it accepted or not."
                        )
                        h += 1

    writeList("vaccine requsets", list)
    if h > 0:
        k = str(
            input(
                "there are requstess didn't List if they accepted or not.\npress 1 if you want to edit that: "
            )
        )
        if k == "1":
            AcceptReservation()
        else:
            print("wrong input")


def checkrequest(specList):
    list = callList("vaccine requsets")
    if list == []:
        print("you don't make requset")
    else:
        for item in list:
            if item[0] == specList[1]:
                if item[3] == 0:
                    print(
                        f"the admins didn't accept your requset yet for {item[2]} vaccine"
                    )
                elif item[3] == "1":
                    print(f"the admins refuse your requset for {item[2]} vaccine")
                else:
                    print(
                        f"the admins accept your requset for {item[2]} vaccine and the Schedule your vaccination on the day {item[3]}"
                    )


def BackUp():
    list = ["vaccine requsets", "Vaccination centers", "regestData"]
    for item in list:
        x = callList(item)
        writeList(f"{item}BU", x)


def checkBU():
    list = ["vaccine requsets", "Vaccination centers", "regestData"]
    for item in list:
        x = callList(item)
        y = callList(f"{item}BU")
        if x != y:
            writeList(item, y)


checkBU()
y = "1"
while y == "1":
    fopen()
    y = str(input("\ndo you want to reenter the login page(1 for yes and 2 for no): "))
    print("\n")
