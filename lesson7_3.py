import random

def play_game(): 
        min=1
        max=10
        target=random.randint(1,10)
        count=0
        print("猜數字遊戲")
        while True:
            count+=1
            keyin=int(input(f"猜數字範圍{min}-{max}:"))
            if keyin>=min and keyin<=max:
                if keyin==target:
                    print(f"賓果!答對了!答案是{target}")
                    break
                elif keyin>target:
                    print("猜錯了!再小一點!")
                elif keyin<target:
                    print("猜錯了!再大一點!")    
                print(f"你已經猜了{count}次")
            else:
                print("請輸入提示範圍內的數字:")
        

while True:
    play_game()
    play_again=input("請問還要繼續嗎?(y,n)")
    if play_again=='n'or'N':
        print("遊戲結束")
        break
    