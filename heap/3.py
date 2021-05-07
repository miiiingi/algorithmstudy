# 일단 큐를 구현
# 그리고 최댓값을 어떻게 뺄지 고민 해보자
import collections
import heapq
def solution(operations) : 
    operations = collections.deque(operations)
    answer = [] 
    while operations : 
        op = operations.popleft()
        imp, num = op.split(' ')
        if imp == 'I' : 
            answer.append(int(num))
        if len(answer) != 0 : 
            if imp == 'D' and int(num) == -1 : 
                heapq.heapify(answer)
                heapq.heappop(answer)
            elif imp == 'D' and int(num) == 1 :
                max_heap = [] 
                use_heap = [] 
                for item in answer : 
                    heapq.heappush(max_heap, (-item, item))
                heapq.heappop(max_heap)
                for elem in max_heap : 
                    use_heap.append(elem[1])
                heapq.heapify(use_heap)
                answer = use_heap
        else : 
            continue
    if len(answer) == 0 :
        return [0, 0]
    else : 
        return [max(answer), min(answer)]
answer = solution(['I 7', 'I 5', 'I -5', 'D -1'])
print(answer)