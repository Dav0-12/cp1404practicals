"""Questions to build file manipulation skills"""


# 1. Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

name = input("Name: ")
outfile = open("name.txt", "w")
print(name, file=outfile)
outfile.close()



# (In the same file, but as if it were a separate program) 
# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

infile = open("name.txt", "r")
name = infile.read()
print(f"Your name is {name}")
infile.close()



# Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds
# them together then prints the result, which should be... 59.

NUMBER_OF_LINES_TO_ADD = 2

infile = open("name.txt", "r")
result = 0
for i, line in enumerate(infile):
    if i == NUMBER_OF_LINES_TO_ADD:
        break
    else:
        result += int(line)
print(result)
infile.close()



# Now write a fourth block of code that prints the total for all lines in numbers.txt 
# or a file with any number of numbers.

infile = open("name.txt", "r")
result = 0
for line in infile:
    result += int(line)
infile.close()
