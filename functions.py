# Define the filepath
FILEPATH = "todos.txt"


# Define a function to open the file - note the default arguments
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


# Define a function to write on the file - note the default arguments
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

