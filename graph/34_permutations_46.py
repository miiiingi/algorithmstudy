# 재귀를 직관적으로 이해할 수 있는 사고력 기르기 !! 복습 필수 !! 
# 어떻게 이렇게 생각해내지..?
# 함수 안에서만 존재해도 되는 지역변수는 그냥 선언 해주고, 전역변수는 self로 선언해줘서 클래스내에서 다 쓸 수 있도록 ! 좀 더 파이썬 스럽게 코드 짜는 것 연습
class Solution : 
    result = [] 
    element_prev = []
    def permute(self, num) : 
        self.dfs(num)
        return self.result
    def dfs(self, elements) :  
        if len(elements) == 0 :
            self.result.append(self.element_prev[:])
        for e in elements : 
            element_next = elements[:]
            element_next.remove(e)
            self.element_prev.append(e)
            self.dfs(element_next)
            self.element_prev.pop()

answer = Solution().permute([1,2,3])
print(answer)