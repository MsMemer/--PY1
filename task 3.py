def delete(list_, index=None):
    if index == None:
        list_new = list_[:-1]
    else:
        list_l = list_[:index]
        list_r = list_[index + 1:]
        list_new = list_l + list_r
    return list_new

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
