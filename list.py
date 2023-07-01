print('-' * 10)

list = "list is MUTABLE and denoted by square bracket'[]'"
print(list)

empid = [12, 55, 22, 6, 5656, 6, 5, 69]

# forward indexing --> getting position of data
print('forward indexing : ' + str(empid[3]))

# reverse indexing ---> getting position of data from end of list
empid_reverse = str(empid[-1])
print('forward indexing : ' + empid_reverse)
"\n"
"\n"

# find index of the data in list
print('index of given number in a list : ' + str(empid.index(6)))
"\n"

# insert new element at given location/index
emp_numbers = [101, 201, 301, 401, 777]
# syntax --> list_mane.insert(location,data_u_need to insert)
inserting_new_element = emp_numbers.insert(4, 101)
print('new list : ' + str(emp_numbers))

inserting_new_element_1 = emp_numbers.insert(-1, 101)
print('new list_with_reverse_index_1 : ' + str(empid))

inserting_new_element_2 = emp_numbers.insert(-2, 'adarsh')
print('new list_with_reverse_index_2 : ' + str(empid))

# adding new elements to list
emp_numbers.append(500)
print('APPEND : ' + str(emp_numbers))

# adding multiple elements to a list
emp_numbers.extend([45, 'PY', 'MachineLearning', 6699])
print('EXTEND : ' + str(emp_numbers))

# removing elements from list
emp_numbers.remove('PY')
print('REMOVE : ' + str(emp_numbers))

# deleting elements using index number from list
emp_numbers.pop(2)
print('POP : ' + str(emp_numbers))

# deleting last element from list
emp_numbers.pop()
print('POP_1 : ' + str(emp_numbers))

# getting count of dplicate elements in list
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
p = list.count(20)
print('DUPLICATE : ' + str(p))

# sorting list in ascending order
asc_list = [78, 55, 44, 5, 2, 2, 66, 9, 21, 4, 554, 45, 45, 454, 5, 45]
asc_list.sort()
print('asc_list : ' + str(asc_list))

# for decending order
asc_list_1 = [78, 55, 44, 5, 2, 2, 66, 9, 21, 4, 554, 45, 45, 454, 5, 45]
asc_list_1.sort(reverse=True)
print('asc_list_1 : ' + str(asc_list_1))


# copy a list
new_py_list = list.copy()
print('new_py_list : ' + str(new_py_list))


# for updating an element in list

new_py_list[5] = 'java'
print('new_py_list : ' + str(new_py_list))
















print('-' * 10)
