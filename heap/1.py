import heapq
def solution(scoville, K) : 
    heapq.heapify(scoville)
    count = 0 
    while scoville : 
        try : 
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            combine = first + second * 2
            count += 1
            heapq.heappush(scoville, combine)
            if scoville[0] >= K : 
                return count
        except :
            return -1
answer = solution([1,2,3,9,10,12], 1000)
print(answer)