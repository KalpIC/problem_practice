
# Binary Search

# def find(ordered_list, element_to_find):
#     start_index = 1
#     if len(ordered_list)%2==0: #even
#         end_index = len(ordered_list)-1
#     elif len(ordered_list)%2!=0: #odd
#         end_index = len(ordered_list)
#     else:
#         print("something wrong with list")
#
#     while True:
#         middle_index = (end_index - start_index) / 2
#         middle_index = int(middle_index)
#         print("m", middle_index)
#
#         if middle_index < start_index or middle_index > end_index or middle_index < 0:
#             return False
#
#         middle_element = ordered_list[middle_index]
#         if middle_element == element_to_find:
#             return True
#         elif middle_element < element_to_find:
#             end_index = middle_index
#         else:
#             start_index = middle_index
#
#
# if __name__ == "__main__":
#     l = [2, 4, 6, 8, 10]
#     e = int(input("Enter element to search in list"))
#
#     print(find(l, e))



def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return print("Your Element is in list")
    return print("Your Element is not in list")


if __name__ == "__main__":
    l = [2,3,5,6,7,8,9,10,14,15,18,20]
    e = int(input("Input no. to search in list"))
    find(l,e)





