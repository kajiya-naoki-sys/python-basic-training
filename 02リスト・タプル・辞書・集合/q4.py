A = {1, 2, 3}
B = {2, 3, 4}

#和集合
print("和集合：", end='')
print(A | B)

#積集合
print("積集合：", end='')
print(A & B)

#差集合
print("差集合：", end='')
print(A - B | B - A)
print("　　　　", end='')
print((A | B) - (A & B))