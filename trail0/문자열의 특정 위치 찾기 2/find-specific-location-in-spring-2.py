words = ["apple", "banana", "grape", "blueberry", "orange"]

target = input().strip()
count = 0
for word in words:
    if word[2]==target or word[3]==target:
        print(word)
        count += 1

print(count)