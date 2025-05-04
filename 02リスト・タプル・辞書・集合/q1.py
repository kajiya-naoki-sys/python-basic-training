num_lis = [3, 1, 4, 1, 5, 9, 2, 6, 5]
#重複削除したのち，リスト型にキャスト
num_lis = list(set(num_lis))
#降順にソート
num_lis.sort(reverse=True)

print(num_lis)