list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

summa_unique_list = sum(set(list_))
lenth_unique_list = len(set(list_))
mean_list = summa_unique_list / lenth_unique_list

print(summa_unique_list)
print(lenth_unique_list)
print(round(mean_list, 5))
