# Exercise 1

l_1 = [1,11,14,5,8,9]
def less_than_ten(list):
    result=[]
    for number in list:
        if number < 10:
            result.append(number)

    return result

print(less_than_ten(l_1))

# Exercise 2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge_n_sort(list_1,list_2):
    result = [*list_1,*list_2]
    result.sort()
    return result

print(merge_n_sort(l_1,l_2))