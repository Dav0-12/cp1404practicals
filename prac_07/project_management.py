"""
Prac 07 - Project Management
Estimated Duration: 60 minutes
Actual Duration:
"""

from prac_07.project import Project
import datetime

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    projects = []
    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Please enter a filename to load from: ")
            projects = load_project_data(filename)
        elif choice == "D":
            display_projects(projects, False)  # No indexing included
        elif choice == "S":
            filename = input("Please enter a filename to load from: ")
            save_project_data(filename, projects)
        elif choice == "U":
            display_projects(projects, True)  # Indexing included
            selected_project = int(input("Project choice: "))
            print(projects[selected_project])

            completion = int(input("New Percentage: "))
            if completion != "":
                projects[selected_project].completion = completion

            priority = input("New priority")
            if priority != "":
                projects[selected_project].priority = priority
        elif choice == "A":
            print("Let's add a new project!")
            name = input("Name: ")
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            estimate = float(input("Cost estimate: "))
            completion = int(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, estimate, completion))
        elif choice == "F":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()



        else:
            print("Not a valid choice")
        print(MENU)
        choice = input(">> ").upper()





def load_project_data(filename):
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()
        for row in in_file:
            row = row.split("\t")
            projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    return projects


def display_projects(projects, include_indexing):
    if include_indexing:
        for i, project in enumerate(projects):
            print(f"{i}  {project}")


    else:
        print("Incomplete projects:")
        for project in projects:
            if not project.is_complete():
                print(f"  {project}")

        print("Complete projects:")
        for project in projects:
            if project.is_complete():
                print(f"  {project}")


def save_project_data(filename, projects):
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            formatted_project = "\t".join(*project)
            print(f'{formatted_project}')


main()
