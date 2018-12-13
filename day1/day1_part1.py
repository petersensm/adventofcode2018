from sys import argv
import operator

script, input_file = argv

# lookup table
ops = { "+": operator.add, "-": operator.sub }

# get input
in_file = open(input_file)
input = in_file.read()

# print(type(input)) str
# split the string into a list of strings
input_list = input.split()

# now take each item and pull off the operator and the number
#first_element = input_list[0]

#print(first_element[0])
#print(first_element[1:])
'''
part 1
    find the final frequency if starting with 0 and adjusting by each element in the list
'''
def calc_frequency():
    print('trying my loop')
    frequency = 0

    for i in input_list:
        #print(i[0])
        #print(i[1:])
        frequency = ops[i[0]](frequency, int(i[1:]))
        print(i, frequency)

calc_frequency()
