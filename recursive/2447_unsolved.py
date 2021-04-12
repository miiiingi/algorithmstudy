def blank(n) : 
    print('{}\n{}\n{}'.format(' '*n, ' '*n, ' '*n)) 
def star(n) : 
    if n == 3 :  
        return '***\n* *\n***'
    else : 
        return print('{}{}{}\n{}{}{}\n{}{}{}'.format(star(n//3),star(n//3),star(n//3),star(n//3),blank(n//3),star(n//3),star(n//3),star(n//3),star(n//3),))

answer = star(9)
print(answer)