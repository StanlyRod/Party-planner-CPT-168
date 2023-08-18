import csv
import sys

#Author: Ramon Stanly Rodriguez
"""
Party planner the final project of the CPT-168 class

the purpose of this program is to receive data from a user
such as attendee name, attendee type can be member guest or student
and the food of their choice, after receive all the data entered by the user
this program will save all that information into a csv file named partyplanner.csv
that is going to be used by the program to retrieve any of the data whenever is need it
"""

CSVFILE = "partyplanner.csv"

#write the entries to a csv file
def WriteTocsv(ln):
    try:    
        with open(CSVFILE, "a", newline="") as Wfile:
                write = csv.writer(Wfile)
                write.writerows(ln)
    except PermissionError as err:
        print("Permission error, the file might be open, please close the file", err)
        print()    


#reads entries of the csv file and returns the data
def ReadCsv():
    try:
        data = []
        with open(CSVFILE, newline="") as rfile:
            reader = csv.reader(rfile)
            for row in reader:
                data.append(row)
        return data

    except FileNotFoundError as err:
        print(f"Error can not find the file\n{err}")
        print()
        sys.exit()


#count and display the total amount of food choices
def foodCounter():
    csvDataFile = ReadCsv()

    chicken    = 0
    beef       = 0
    sushi      = 0
    vegetarian = 0
    pizza      = 0

    for row in csvDataFile:
        if row[2] == "chicken":
            chicken += 1
        elif row[2] == "beef":
            beef += 1
        elif row[2] == "vegetarian":
            vegetarian += 1
        elif row[2] == "sushi":
            sushi += 1
        elif row[2] == "pizza":
            pizza += 1
    
    print(f"Total orders of chicken:\t{chicken}")
    print(f"Total orders of beef:\t\t{beef}")
    print(f"Total orders of sushi:\t\t{sushi}")
    print(f"Total orders of vegetarian:\t{vegetarian}")
    print(f"Total orders of pizza:\t\t{pizza}")
    print()


#count number of members guests and students
def TotalMembersGuestsStudents(message, mg):
    csvDataFile = ReadCsv()
    count = 0
    for n, eachPerson in enumerate(csvDataFile, start=1):
        if eachPerson[1] == mg:
            count += 1
    print(message, count)

    
#show each member from the csv file
def ListMembers():
    csvDataFile = ReadCsv()
    for eachMember in csvDataFile:
        if eachMember[1] == "Member":
            print(f"{eachMember[0]:<10} {eachMember[1]:<10} {eachMember[2]:<10} {'$':>5}{eachMember[3]:>1}")
            print()


#show each guest from the csv file
def ListGuests():
    csvDataFile = ReadCsv()
    for eachGuest in csvDataFile:
        if eachGuest[1] == "Guest":
            print(f"{eachGuest[0]:<10} {eachGuest[1]:<10} {eachGuest[2]:<10} {'$':>2}{eachGuest[3]:>1}")
            print()


#show each student from the csv file
def ListStudents():
    csvDataFile = ReadCsv()
    for eachStudent in csvDataFile:
        if eachStudent[1] == "Student":
            print(f"{eachStudent[0]:<10} {eachStudent[1]:<10} {eachStudent[2]:<10} {'$':>5}{eachStudent[3]:>1}")
            print()


#show each members, guests and students with the food choices and fee
def ListMembersGuestsStudents():
    csvDataFile = ReadCsv()
    if len(csvDataFile) == 0:
        print("The csv file is empty please add some values.\n")
        print()
    else:
        for i, mg in enumerate(csvDataFile, start=1):
            print(f"{i:<5} {mg[0]:<10} {mg[1]:<10} {mg[2]:<10} {'$':>4}{mg[3]:>1}")
            print()
        print()


#count and display the total fees
def TotalFees():
    fees = [] #empty list
    csvDataFile = ReadCsv()

    for eachFee in csvDataFile:
        if eachFee[3] != 0:
            fees.append(eachFee[3])
    
    #converts each item in the fees list in integer
    for e in range(0, len(fees)):
        fees[e] = int(fees[e]) #converts each item in the fees list to integer

    feesTotal = sum(fees) #adds each item in the fees list and returns the total
    print(f"Total Fees Paid by all attendees: ${feesTotal}")
    print()


#show all the commands
def Commands():
    print()
    print("COMMAND MENU")
    print("add  => Add members, guests or students")
    print("lm   => List all members")
    print("lg   => List all guests")
    print("ls   => List all students")
    print("lmgs => List all members, guests and students")
    print("cmd  => Display the list of commands")
    print("rp   => Display a full report")
    print("exit => Exit the program")
    print()


"""
show report function
show a full report with the members, guests and students with the name and the food choice
this function can also show the total numbers of members guests and students
can also show the total fees and the total of food choice
"""
def Report():
    ListMembersGuestsStudents()
    TotalMembersGuestsStudents("Total Members:\t","Member")
    TotalMembersGuestsStudents("Total Guests:\t", "Guest")
    TotalMembersGuestsStudents("Total Students:\t","Student")
    TotalFees()
    foodCounter()
   

"""
prompts the user 
to enter a food choice from the food menu 
and returns the food chosen by the user
"""
def MenuChoices():
    foodMenu = {"c": "chicken", "b": "beef", "v": "vegetarian", "s": "sushi", "p": "pizza"}

    validation = True
    while(validation):
        print("If you want chicken type 'c'")
        print("for beef type            'b'")
        print("for vegetarian type      'v'")
        print("for sushi type           's'")
        print("for pizza type           'p'")

        food = input("Enter Your Menu Choice: ")
        foodL = food.lower()
        print()

        if(foodL in foodMenu):  
            return foodMenu[foodL]
        else:
            print("Invalid Input, Pleae Try Again.")
            print()
            validation = True


#prompts the user to enter the attendee name, member, guest or student then save the information in a csv file
def AddMembersGuestsStudents():
    m = "Member"
    g = "Guest"
    s = "Student"
    price = 21 #regular fee for members and guests
    studentFee = 10 #fee for students

    members  = [] #empty list that only holds members
    guests   = [] #empty list that only holds guests
    students = [] #empty list that only holds students

    GuestMemberOrStudent = [] #empty list that can hold members guests or students

    name = input("Enter attendee name: ") 
    print()

    validation = True
    while(validation):
        print("For member enter letter  'm'")
        print("For guest  enter letter  'g'")
        print("For student enter letter 's'")

        MGS = input("Enter attendee type: ")
        print()
        if(MGS.lower() == "m"):
            food = MenuChoices()
            GuestMemberOrStudent = [name, m, food, price]
            members.append(GuestMemberOrStudent)
            WriteTocsv(members)
            print(members[0][0], members[0][1], members[0][2], "was added.")
            validation = False   

        elif(MGS.lower() == "g"):
            food = MenuChoices()
            GuestMemberOrStudent = [name, g, food, price]
            guests.append(GuestMemberOrStudent)
            WriteTocsv(guests)
            print(guests[0][0], guests[0][1], guests[0][2], "was added.")
            validation = False
        
        elif(MGS.lower() == "s"):
            food = MenuChoices()
            GuestMemberOrStudent = [name, s, food, studentFee]
            students.append(GuestMemberOrStudent)
            WriteTocsv(students)
            print(students[0][0], students[0][1], students[0][2], "was added.")
            validation = False

        else:
            print("Invalid Input, Please Try Again")
            print()
            validation = True


#main function
def main():
    print("Welcome To The Party Manager Program")
    Commands()

    while(True):
        command = input("Command: ")
        print()

        if(command.lower()   == "add"):
            AddMembersGuestsStudents()
        elif(command.lower() == "lm"):
            ListMembers()
        elif(command.lower() == "lg"):
            ListGuests()
        elif(command.lower() == "ls"):
            ListStudents()
        elif(command.lower() == "lmgs"):
            ListMembersGuestsStudents()
        elif(command.lower() == "cmd"):
            Commands()
        elif(command.lower() == "rp"):
            Report()
        elif(command.lower() == "exit"):
            break
        else:
            print("Invalid command, please try again or type 'cmd' to display the list of commands")
            print()
    
if __name__ == "__main__":
    main()





