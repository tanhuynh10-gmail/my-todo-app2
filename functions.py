FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and
    return the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):

    """" Write the to-do items list in the text file """

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
def state_of_water(temperature: float):
    min_gas_temp = 100
    min_solid_temp = 0

    if temperature >= min_gas_temp:
        return "gas"
    elif temperature <= min_solid_temp:
        return "solid"
    else:
        return "liquid"

def count(phrase):
    return phrase.count('.')

def convert_feetinch2meter(feet: float, inches: float):
    return feet * 0.3008 + inches * 0.0254

if '__name__' == '__main__':
    print("Hello")

