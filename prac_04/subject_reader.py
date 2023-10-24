"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    parts = []
    for line_count, line in enumerate(input_file):
        line = line.strip()  # Remove the \n
        parts.append(line.split(','))  # Separate the data into its parts
        parts[line_count][2] = int(parts[line_count][2])  # Make the number an integer (ignore PyCharm's warning)
    input_file.close()
    return parts


def display_data(data):
    """Display data in the format, 'subject' is taught by 'lecturer' and has 'number of students' students"""
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]} and has {data[i][2]} students")


main()
