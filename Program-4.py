# Problem-4:  Get the total count of number list in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
#     (examples)
#     input: [1,2,8,9,12,46,76,82,15,20,30]
#     Output:
#         {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}

def checkMultiple(num, input_arr):
    value = 0
    for i in input_arr:
        if i%num == 0:
            value += 1
    return value

input_arr = list(map(int, input('\nEnter the numbers: ').replace(',', ' ').strip().split()))
output = {}

for i in range(1, 10):
    output[i] = checkMultiple(i, input_arr)

print(output)
