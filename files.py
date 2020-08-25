"""Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).

Create a text file called numbers.txt and save it in your prac_02 directory. Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result, which should be... 59.

Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of numbers."""

# creates a file called name that saves the input using print and file=out_file
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
name = input(str("Enter your name: "))
print("{}".format(name), file=out_file)
out_file.close()

# reads the file name.txt and assigns it to the value name, printing it
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is", name)

# readline twice to read the first 2 lines an assign them values, adding them at the end
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

# for loop for the number of lines adding each to a variable 'total', printing at the end
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total = total + number
in_file.close()
print(total)