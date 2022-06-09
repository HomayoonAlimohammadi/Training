# def has_square(nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             mult = nums[i] * nums[j]
#             if sqrt(mult) == int(sqrt(mult)):
#                 return True 
#     return False 

def make_cube(num, elements):
    temp = num
    for i in range(2, num+1):
        while temp % i == 0:
            elements[i] = elements.get(i, 0) + 1
            if elements[i] % 2 == 0:
                return True, elements
            temp /= i

    return False, elements

def kamel(array):

    n_groups = 1
    elements = {}

    for num in array:
        if not elements:
            ans, elements = make_cube(num, {})

        else:
            # new_elems = get_elements(num)
            # for elem, value in new_elems.items():
            #     elements[elem] = elements.get(elem, 0) + value
                
            # for value in elements.values():
            #     if value % 2 == 0:
            #         elements = {}
            #         n_groups += 1
            ans, elements = make_cube(num, elements)
            if ans:
                elements = {}
                n_groups += 1


    # new_elems = get_elements(num)
    # for elem, value in new_elems.items():
    #     elements[elem] = elements.get(elem, 0) + value
        
    for value in elements.values():
        if value % 2 == 0:
            elements = {}
            n_groups += 1
    
    return n_groups


n = int(input())
line = [int(i) for i in input().split()]
print(kamel(line))