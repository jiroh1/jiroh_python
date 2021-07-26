
class Solution:
    def solution(n): # 피보나치의 수열에서 n＜=2 일 경우
        sol = [0, 1]
        for i in range(n):
            sol.append(sol[-1] + sol[-2])
            # print(sol[-1],sol[-2])
        # print(sol) #값이 축적이 되는지 확인 ex) 4일경우 [0, 1, 1, 2, 3, 5]
        del sol[-1] # 마지막 값은 빼고 확인
        #print(sol,"2")
        #print(sol[-2],"-2번째")
        #print(sol[-3],"-3번째")
        print(sol[-2]+sol[-3])

if __name__ == '__main__':
    n = int(input("숫자를 입력하세요 :"))
    Solution.solution(n)

    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...