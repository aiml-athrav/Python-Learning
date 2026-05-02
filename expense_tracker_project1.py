#PROJECT 1

expenselist = [] 

print("!!! WELCOME TO EXPENSE TRACKER !!!")

while True:
    print("======MENU======")
    print("to add expenses enter 1")
    print("to view all expenses enter 2")
    print("to view total amount expended enter 3")
    print("to exit the enter 4")

    choice = int(input("Enter your choice :"))


    if(choice == 1):
        date = input("kis date prr karacha kraa hai :")
        category = input("kis type k karcha kara hai :")
        description = input("aur detail de do :")
        amount = float(input("kitne pese udaye hai janni :"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount,
        }

        expenselist.append(expense)
        print("janni !! daal diya tera kharcha")

    elif(choice == 2):
        if(len(expenselist) == 0):
            print("janni jake kharcha kr kanjus mt bann ")
        else:
            print(" janni teraa sara expendeture :")
            count = 1
            for kharcha  in expenselist:
                print(f"kharcha number {count} --> {kharcha["date"]},{kharcha["category"]},{kharcha["description"]},{kharcha["amount"]} ")
                count = count +1

    elif(choice == 3):
        total = 0
        for kharcha in expenselist:
            total = total + kharcha["amount"]
        print(" dekh le janni kitna udaa chuka hai be tu", total)

    elif(choice == 4):
        print(" janni tu is duniya se bhar aa gay hai .. ")
        break

    else:
        print("janni phele instruction pdhna sikh")
