def validate_number_egg(number_egg):
    if type(number_egg) == str:
        return "input integer"
    elif number_egg < 1:
        return "out of range"

def number_to_egg(number_egg):
    cost_egg = 4
    number_egg = 0
    dozen_egg = 12
    if number_egg < 12 :
        return number_egg*cost_egg
    elif number_egg >= 12 :
        return cost_egg == 3 and number_egg*cost_egg
    elif dozen_egg >= 5 :
        return cost_egg == 35

def display_number_egg(number_egg):
    result = validate_number_egg(number_egg)
    if type(result) == int:
        return number_to_egg(result)
    else:
        return result
