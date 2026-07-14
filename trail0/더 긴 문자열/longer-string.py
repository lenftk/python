# 두 단어 입력받기
word1, word2 = input().split()

# 각 단어의 길이 계산
len1 = len(word1)
len2 = len(word2)

# 조건에 따른 출력
if len1 > len2:
    print(f"{word1} {len1}")
elif len2 > len1:
    print(f"{word2} {len2}")
else:
    print("same")