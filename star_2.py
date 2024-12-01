import re

with open("location_ids.txt",'r') as file:
    data = file.read()
location_ids = re.findall(r'\d+',data)
location_ids_int = [int(num) for num in location_ids]

left_list=[]
right_list=[]
def alternate_init():
    left =1
    for id in location_ids_int:
        if left ==1:
            left_list.append(id)
            left=0
        else:
            right_list.append(id)
            left=1
    left_list.sort()
    right_list.sort()

alternate_init()
# print(location_ids_int)
similarity_score_result=0

for id in left_list:
    count = right_list.count(id)
    similarity_score_result += id*count

print(similarity_score_result)
