import json

with open("ru_all.json","r",encoding="utf-8_sig") as f:
    num_json = json.load(f)

while True:
    str =""
    color = ""
    ru_num = 0
    ru_str = ""
    point = 0
    end=""
    strs={}
    bet = 0
    temp_dict={}

    #0 x15 num x5 color x2
    while True:
        str = input("数字に賭けるなら1,色に賭けるなら2,賭け終わるなら3を入力: ")
        if str == "3":
            print("以下の内容で確定しますか？")
            for i in strs:
                print(f"{i} = {strs[i]} ",end=",")
            print()
            while True:
                end = input("y or n ?")
                if end=="y":
                    break
                elif end=="n":
                    strs=[]
                else:
                    print("入力し直してください")
                    continue
            if end=="y":
                break
        elif str == "2":
            while True:
                color = input("赤に賭けるならred,黒に賭けるならblackを入力: ")
                if color == "red" or color == "black":
                    bet = int(input("ベット数を入力: "))
                    break
                else:
                    print("入力し直してください。\n\n")
            temp_dict = {color:bet}
            strs.update(temp_dict)
        elif str == "1":
            while True:
                number = input("賭ける数字を入力: ")
                if int(number) >= 0 and int(number) <= 29:
                    bet = int(input("ベット数を入力: "))
                    break
                else:
                    print("入力し直してください。\n\n")
            temp_dict = {number:bet}
            strs.update(temp_dict)

    ru_num = int(input("結果を入力してください: "))
    for i in range(len(num_json)):
        if num_json[i][1] == ru_num:
            ru_str = num_json[i][0]

    for i in strs:
        try:
            if i == ru_str:
                point += strs[i] * 2
            elif int(i) == ru_num:
                if int(i) == 0:
                    point += strs[i] * 15
                else:
                    point += strs[i] * 5
        except Exception:
            pass

    for i in strs:
        point -= strs[i]

    print(f"利益は {point}")
    input("進めるためにはEnterを押してください\n")
