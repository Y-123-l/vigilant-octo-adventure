import random

answer = random.randint(1, 100)
count = 0
limit = 7
win = False

print(f"我想了一个 1 到 100 的数字，你有 {limit} 次机会")

while count < limit:
    text = input("请输入你猜的数字：")

    if not text.isdigit():
        print("只能输入数字，这次不算数")
        continue

    guess = int(text)
    count += 1

    if guess < answer:
        print(f"小了，还剩 {limit - count} 次")
    elif guess > answer:
        print(f"大了，还剩 {limit - count} 次")
    else:
        win = True
        print(f"猜对了！你用了 {count} 次")
        break

if not win:
    print(f"机会用完了，答案是 {answer}")
