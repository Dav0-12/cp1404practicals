"""
Prac 07 - Project Management
Estimated Duration: 60 minutes
Actual Duration: 73 minutes
"""

from prac_07.project import Project
from datetime import datetime
from operator import attrgetter

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

DEFAULT_FILE_NAME = "projects.txt"


def main():
    """Allow users to load, update and save project data"""
    projects = []
    projects = load_project_data(DEFAULT_FILE_NAME, projects)
    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Please enter a filename to load from: ")
            projects = load_project_data(filename, projects)
        elif choice == "D":
            display_projects(projects, False)  # No indexing included
        elif choice == "S":
            filename = input("Please enter a filename to save to: ")
            save_project_data(filename, projects)
        elif choice == "U":
            projects = update_existing_project(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "F":
            filter_by_date_and_display(projects)
        else:
            print("Not a valid choice")
        print(MENU)
        choice = input(">> ").upper()
    save_project_data(DEFAULT_FILE_NAME, projects)
    print("Thanks for using this project manager!")


def update_existing_project(projects):
    """Update the completion percentage and the priority of the users chosen project"""
    try:
        display_projects(projects, True)  # Indexing included
        selected_project = int(input("Project choice: "))
        print(projects[selected_project])
        completion = int(input("New Percentage: "))
        if completion != "":
            projects[selected_project].completion = completion
        priority = input("New priority: ")
        if priority != "":
            projects[selected_project].priority = int(priority)
    except ValueError:
        print("Not a valid input.")
    except IndexError:
        print("This project does not exist. No project will be updated.")
    return projects


def filter_by_date_and_display(projects):
    """Display the projects created on or after the users selected date"""
    try:
        date_string = input("Show projects that start after date (dd/mm/yyyy): ")
        start_date = datetime.strptime(date_string, "%d/%m/%Y").date()
        for project in sorted(projects, key=attrgetter("start_date")):
            if project.start_date >= start_date:
                print(f"  {project}")
    except ValueError:
        print("Not a valid date")


def add_project(projects):
    """Prompt the user for project details and return projects with a new project added"""
    print("Let's add a new project!")
    try:
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        estimate = float(input("Cost estimate: $"))
        completion = int(input("Percent complete: "))
        projects.append(Project(name, start_date, priority, estimate, completion))
    except ValueError:
        print("Invalid choice. No new project has been added")
    return projects


def load_project_data(filename, projects):
    """Load data from file given by filename. Appends data to projects and then returns it"""
    try:
        with open(filename, "r") as in_file:
            in_file.readline()
            for row in in_file:
                row = row.split("\t")
                projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    except FileNotFoundError:
        print("File not found. No new data loaded.")
    return projects


def display_projects(projects, include_indexing):
    """Display incomplete and complete projects without numbered indexing, or all projects with numbered indexing"""
    if include_indexing:
        for i, project in enumerate(projects):
            print(f"{i}  {project}")
    else:
        print("Incomplete projects:")
        for project in sorted(projects):
            if not project.is_complete():
                print(f"  {project}")

        print("Complete projects:")
        for project in sorted(projects):
            if project.is_complete():
                print(f"  {project}")


def save_project_data(filename, projects):
    """Save project data to the file given by filename"""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f'{project.project}\t{project.start_date.strftime("%d/%m/%Y")}\t{project.priority}\t'
                  f'{project.estimate}\t{project.completion}', file=out_file)


main()
