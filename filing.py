def read_file(file_name):
    """Reads in a file and returns its contents as a string."""
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
        return contents

def read_file_into_list(file_name):
    """Reads in a file and stores each line as an element in a list."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines

def write_first_line_to_file(file_contents, output_filename):
    """Writes the first line of a string to a file."""
    lines = file_contents.strip().split('\n')
    first_line = lines[0]

    with open(output_filename, 'w') as file:
        file.write(first_line)

def read_even_numbered_lines(file_name):
    """Reads in the even-numbered lines of a file."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        even_lines = [line.strip() for index, line in enumerate(lines) if index % 2 == 1]
        return even_lines

def read_file_in_reverse(file_name):
    """Reads a file and returns a list of the lines in reverse order."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        reversed_lines = list(reversed(lines))
        for line in reversed_lines:
            print(line.strip())  # Print the lines in reverse order
        return reversed_lines

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    # print(read_file_into_list("sampletext.txt"))
    # write_first_line_to_file(file_contents, "online.txt")
    # print(read_even_numbered_lines("sampletext.txt"))
    # print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()