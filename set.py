print('SET is  denated by {}')
print('\n')


# adding elements to set
set = {1}
set.add(100)
print(set)


# DELETION OPERATION
    # REMOVE
    # if element then delete
    # if not then return keyerror - hard delete

set.remove(100)
print(set)

# set.remove(100)

    # DISCARD
    # if element then delete
    # if not then skip(no error) -- soft delete

set2 = {45,25,'python','ML'}

set2.discard(45)
set2.discard(100)
set2.discard('DS')

print(set2)

   # Delete from Random Location , returns the deleted element

print('\n\n')
print(set2.pop())


























































































