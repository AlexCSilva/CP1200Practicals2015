"""
Pythonville Hospital Medical Records Manager

Created: 05/04/2013 by Trevor Andersen
"""
CHECK_OPTION = "1"
CREATE_OPTION = "2"
VIEW_OPTION = "3"
ADD_OPTION = "4"
QUIT_OPTION = "5"
PATIENTS_FILE = "patients.txt"

def main():
    print('Pythonville Hospital Medical Records Manager')
    print()
    
    displayMenu()
    option = input("Enter your choice: ")

    while option != QUIT_OPTION:
        if option == CHECK_OPTION:
            checkIfPatientInSystem()
        elif option == CREATE_OPTION:
            createNewRecord()
        elif option == VIEW_OPTION:
            viewRecord()
        elif option == ADD_OPTION:
            addRecord()
        else:
            print("Please enter a valid option.")

        displayMenu()
        option = input("Enter your choice: ")        

def displayMenu():
    print("1. Check if a patient is in the system")
    print("2. Add a new patient to the system")
    print("3. View medical record")
    print("4. Add to medical record")
    print("5. Quit")    

# gets the first and last name for a patient from the user
# the file of patients is then checked for that name
# whether the record exists is displayed to the user
def checkIfPatientInSystem():
    firstName, lastName = getNames()
    
    if isPatientInSystem(firstName, lastName):
        print(firstName, lastName, "is in the system.")
    else:
        print(firstName, lastName, "is NOT in the system.")

def createNewRecord():
    print("createNewRecord")

def viewRecord():
    print("viewRecord")

def addRecord():
    print("viewRecord")

# gets a first and last name from the user
# makes sure they're not blank
# returns firstName, lastName
def getNames():
    firstName = input("Enter first name: ")
    while firstName == "":
        print("Name cannot be blank!")
        firstName = input("Enter first name: ")
        
    lastName = input("Enter last name: ")
    while lastName == "":
        print("Name cannot be blank!")
        lastName = input("Enter last name: ")

    return firstName, lastName

# parameters are the first and last names of a patient
# searches the file for a line with those names
# return True if the patient is found
def isPatientInSystem(firstName, lastName):
    result = False
    fileIn = open(PATIENTS_FILE, 'r')

    for line in fileIn:
        if line.strip() == firstName + " " + lastName:
            result = True
            break

    fileIn.close()
    return result

main()
