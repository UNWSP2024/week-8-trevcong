#AUTHOR: Trevor Conger UNWSP
#DATE: 10/25/24
#TITLE: Courses!

#PSEUDOCODE
#-------------------------------------------------------------------------------------------------------------------
# While True
#   Call function
#      Ask user for COURSEID and NAME OF COURSE 
#      ADD COURSE TO DICT  
#        Do you want to add more to courses? 
#           if NO: BREAK
#   While True
#       Ask what course they are looking for
#           IF Course in courses
#           THEN return back to user that KEY:VALUE from the DICT
#       IF not respond that it is not found
#   ASK user if they want to search again for another 
#       IF NO: BREAK
#
#---------------------------------------------------------------------------------------------------------------------


courses = {}

def main():
    while(True):
        func()

        addCourse = input("Do you want to add another course? (yes/no): ").lower()
        if addCourse == "no":
            break
    while(True):
        subject = input("\nWhat course subject are you looking for? (e.g., COS): ").strip().upper()

        searchCourses(subject)

        search_again = input("Do you want to search for another subject? (yes/no): ").lower()
        if search_again == "no":
            break



def func():
    courseID = input("Enter the course ID (e.g., COS 2005): ")
    courseDescription = input("Enter the course description (e.g., Python programming): ")
    courses[courseID] = courseDescription

def searchCourses(subject):
    foundCourses = False
    print(f"\nCourses with the subject '{subject}':")

    for courseID, courseDescription in courses.items():
        if courseID.startswith(subject):
            print(f"{courseID}: {courseDescription}")
            foundCourses = True

    if not foundCourses:
        print(f"No courses found for subject '{subject}'.")

if __name__ == "__main__":
    main()