#ある文字列をSとする
S=input("ある文字列")
for index in range(len(S)):
    if S[index] in S[index+1:]:
        print("Ouch!")
        break
    elif index == len(S)-1:
        print("重複はありません")
    else:
        continue
