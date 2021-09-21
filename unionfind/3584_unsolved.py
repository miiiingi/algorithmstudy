import collections
def find(number, find_list) : 
    find_list.append((number, floor[number - 1]))
    if graph[number] == number : 
        return find_list 
    else : 
        graph[number] = find(graph[number], find_list)
        return find_list
N = int(input())
for i in range(N) : 
    graph = collections.defaultdict(list)
    num_v = int(input())
    floor = [0] * num_v
    find1_list = list()
    find2_list = list()
    for num_n in range(num_v - 1) : 
        parent, child = map(int, input().split())
        graph[child].append(parent)
        floor[child - 1] = floor[parent - 1] + 1
    find1, find2 = map(int, input().split())
    find1_list = find(find1, find1_list)

