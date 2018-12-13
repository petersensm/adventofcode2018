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
part 2
    find the first result frequency to be repeated
'''

# tests
testList1 = ['+1', '-1'] # 0
testList2 = ['+3', '+3', '+4', '-2', '-4'] # 10

def calc_part_2(list_o_stuff):
    print('running calc_part_2')
    # initialize dict
    frequency_ls = []
    frequency = 0
    solution = 0
    while solution == 0:
        for i in list_o_stuff:
            #print(i[0])
            #print(i[1:])
            frequency = ops[i[0]](frequency, int(i[1:]))
            print(i, frequency)
            if frequency in frequency_ls:
                print('this is the second ', frequency)
                print("done!")
                solution = 1
                break
            else:
                frequency_ls.append(frequency)
                #print(frequency_ls)
    print("BYE NOW")

print('test 1 result should be 0')
calc_part_2(testList1)

print('test 2 result should be 10')
calc_part_2(testList2)

print("running on test input")
calc_part_2(input_list)
