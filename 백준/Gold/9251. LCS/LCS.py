import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

# LCS 테이블을 올바르게 초기화
LCS = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
# LCS = [[0]*(len(str1)+1) for i in range(len(str2)+1)]
# LCS = [[0]*(len(str1)+1)]*(len(str2)+1) 한열만들고 그걸 참조하는 배열을 만들기때문에 잘못됨!
# print(LCS)

# if str1[x] == str2 [y]   LCS[x][y] = LCS[x-1][y-1]+1
# elif str1[x] != str2[y]  LCS[x][y] =max(LCS[x-1][y], LCS[x][y-1])

# print(str1[0])

#LCS table calculation
for i in range(1,len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1]==str2[j-1]:
            LCS[i][j] = LCS[i-1][j-1]+1
        elif str1[i-1]!=str2[j-1]:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            
# print(LCS)
print(LCS[len(str1)][len(str2)])