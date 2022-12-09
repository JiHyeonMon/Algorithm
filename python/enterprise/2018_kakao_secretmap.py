#2018 카카오 코딩테스트 - 비밀지도

def solution(n, arr1, arr2):
    answer_num=[]
    answer=[]
    for i in range(n):
        a = ""
        answer_num.append(bin(arr1[i]|arr2[i]))
        answer_num[i] = answer_num[i][2:].zfill(n)
        print(answer_num[i])
        for j in range(n):
            if answer_num[i][j] == '1':
                a += "#"
            else:
                a += " "
        answer.append(a)

    return answer

n = 6
arr1 = 	[46, 33, 33 ,22, 31, 50]
arr2 = 	[27 ,56, 19, 14, 14, 10]
solution(n, arr1, arr2)

'''
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]

매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
'''
