import re
def solution(new_id) : 
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]+', '.', new_id)
    new_id = re.sub('^[.]', '', new_id)
    new_id = re.sub('$[.]', '', new_id)
    if len(new_id) == 0 : 
        new_id = 'a'
    if len(new_id) >= 16 : 
        new_id = new_id[:15]
    if len(new_id) <= 2 : 
        new_id = re.sub('$.','', new_id)
        new_id = new_id[:3]
    return new_id 
answer = solution("...!@BaT#*..y.abcdefghijklm")
answer = solution("z-+.^.")
answer = solution("=.=")
print(answer)