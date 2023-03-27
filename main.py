from function import display_number_egg
from function import number_to_egg

input_number_egg = input()
cost_egg = 4
try:
    try:
        input_number = int(input_number_egg)
    except:
        input_number = float(input_number_egg)
except:
    input_number = str(input_number_egg)
cost = number_to_egg(input_number_egg*cost_egg)
result = display_number_egg(cost)
print(result)
