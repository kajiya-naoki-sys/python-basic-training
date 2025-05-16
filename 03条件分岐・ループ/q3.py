num = 0
while(True) :
    num += 1
    #ontinue：numが5の時は，6行目以降のwhile文の処理を行わず，2行目に戻る．
    if num == 5 : continue
    print(num)
    #break：numが10の時は，ループから抜け出す．
    if num == 10: break

print("end")