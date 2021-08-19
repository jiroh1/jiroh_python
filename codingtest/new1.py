
class Solution:
    def solution(self,n): # 피보나치의 수열에서 n＜=2 일 경우
        if n <= 2:
            return 1

        elif 2<n<=80:  # 피보나치의 수열에서 n>2 일 경우
            k = Solution.res(self,n - 2) + Solution.res(self,n - 1) -1 # 이전 값들을 불러와야 해서 res 라는 function을 만들어서 수열이 돌도록 하였다.
            return k
        else:
            return int(input("숫자를 다시 입력하세요 :")) # 제약사항에 0 <= n <= 80가 있어서 다시 입력하도록 하였다.

    def res(n):
        if n<2:
            return 1
        else:
            k = (n-2) + (n-1)
            return k


if __name__ == '__main__':
    n = int(input("숫자를 입력하세요 :"))
    Solution.solution(n)