import random

answer = random.randint(1, 100)
count = 0

print("我想了一个 1 到 100 之间的数字，你来猜")

while True:
    text = input("请输入你猜的数字：")
    guess = int(text)
    count = count + 1

    if guess < answer:
        print("小了")
    elif guess > answer:
        print("大了")
    else:
        print(f"猜对了！你用了 {count} 次")
        break
