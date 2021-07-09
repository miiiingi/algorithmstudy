# 우선 하나로 옮겨갈 수 있는 단어들의 그래프를 구현
# 구현된 그래프를 바탕으로 BFS를 통해 지정한 지점으로의 최솟값을 계산
import collections
import heapq
def make_graph(begin, words) : 
    graph = collections.defaultdict(list)
    for ind in range(len(words)) : 
        if ind == len(words) - 1 :
            begin = words[ind]
            for ind2 in range(len(words)) : 
                # words[ind2]와 begin을 비교해서 그래프를 구성
                sum_diff = 0
                for word_begin, word_words in zip(begin, words[ind2]) :
                    _sum_diff = abs(ord(word_begin) - ord(word_words))
                    if _sum_diff > 0 :
                        sum_diff += 1
                if sum_diff == 1 : 
                    graph[begin].append(words[ind2])
        for ind2 in range(len(words)) : 
            # words[ind2]와 begin을 비교해서 그래프를 구성
            sum_diff = 0
            for word_begin, word_words in zip(begin, words[ind2]) :
                _sum_diff = abs(ord(word_begin) - ord(word_words))
                if _sum_diff > 0 :
                    sum_diff += 1
            if sum_diff == 1 : 
                graph[begin].append(words[ind2])
        begin = words[ind]
    return graph
def solution(begin, target, words) : 
    if target not in words : 
        return 0
    graph = make_graph(begin, words)
    print(graph)
    visited = collections.defaultdict(int)
    Q = [(0, begin)]
    while Q : 
        cost, start = heapq.heappop(Q)
        if start not in visited : 
            visited[start] = cost
            for desti in graph[start] : 
                heapq.heappush(Q, (cost + 1, desti))
    return visited[target]
answer = solution('hit', 'cog', ["cog", "dot", "dog", "lot", "log", "hot"])
print(answer)
