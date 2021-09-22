import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def find(number) : 
    if friends[number] == number : 
        return number
    else : 
        friends[number] = find(friends[number])
        return friends[number] 
def union(start, end) : 
    parent_start = find(start)
    parent_end = find(end)
    if parent_start != parent_end : 
        if parent_start < parent_end : 
            friends[parent_end] = parent_start
            return parent_start
        elif parent_start > parent_end : 
            friends[parent_start] = parent_end
            return parent_end
N = int(input())
for _ in range(N) :
    answer = 0 
    friends = collections.defaultdict(str)
    num_friends = int(input())
    for n in range(num_friends) : 
        f1, f2 = input().split()
        if f1 not in friends : 
            friends[f1] = f1
        if f2 not in friends : 
            friends[f2] = f2
        p = union(f1, f2)
        for k in friends.keys() : 
            v = find(k)
            if v == p : 
                answer += 1
        print(answer) 
    

