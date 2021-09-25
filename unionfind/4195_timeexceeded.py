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
            for friend in friends.keys() : 
                if friends[friend] == parent_end : 
                    friends[friend] = parent_start
            return parent_start  
        elif parent_start > parent_end : 
            friends[parent_start] = parent_end
            for friend in friends.keys() : 
                if friends[friend] == parent_start : 
                    friends[friend] = parent_end
            return parent_end  
N = int(input())
for _ in range(N) :
    friends = collections.defaultdict(str)
    num_friends = int(input())
    for n in range(num_friends) : 
        answer = 0 
        f1, f2 = input().split()
        if f1 not in friends : 
            friends[f1] = f1
        if f2 not in friends : 
            friends[f2] = f2
        p = union(f1, f2)
        for v in friends.values() :
            if v == p : 
                answer += 1
        print(answer)
    

