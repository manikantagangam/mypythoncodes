# find if an element is present in the list or not
def find_in_list(input_list, search_item):
    for i in range(0, len(input_list)):
        if input_list[i] == search_item:
            return True
    return False

x = find_in_list([2,"y",4], 4)
print(x)
