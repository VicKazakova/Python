src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]
# 1 способ
result = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        result.append(src[i])
print(result)

# 2 способ
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
print(result)
