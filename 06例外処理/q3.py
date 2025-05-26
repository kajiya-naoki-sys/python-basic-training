try:                        #まずはここで，エラーが起こりうる処理を書く
    print(1/0)
except:                     #エラーが起きた場合は，ここに入る
    print("Error")
else:                       #エラーが起きなかった場合は，ここに入る
    print("NO Error")
finally:                    #全体の処理の一番最後にここに入る
    print("FINISH")