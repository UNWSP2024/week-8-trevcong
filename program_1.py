#AUTHOR: Trevor Conger UNWSP
#DATE: 10/25/24
#TITLE: Initials Generator!


#FUNCTION to take in a persons name and turn it into initials. 
def initials_generator(personsName):
    initials = ""
    name_parts = personsName.split()
    
    for part in name_parts:
        initials += part[0].upper() + ". "  

    return initials.strip() 

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)