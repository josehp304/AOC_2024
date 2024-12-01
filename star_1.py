import re
with open("location_ids.txt",'r') as file:
    data = file.read()

location_ids = re.findall(r"\d+",data)
location_ids_int = [int(num) for num in location_ids]
left_list = []
right_list = []

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

sum_distance =0
for i in range(len(left_list)):
    sum_distance+=(abs(left_list[i]-right_list[i]))
print (sum_distance)


