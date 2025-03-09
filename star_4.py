with open("reports.txt","r") as file:
    data = file.read()
arr = data.split("\n")
print(len(arr))

def difference(report):
    flag =0
    for j in range(len(report)-1):
        if (abs(int(report[j])-int(report[j+1]))<1 or abs(int(report[j])-int(report[j+1]))>3 ):
            flag +=1
    return flag
def direction(report):
    flag =0
    if(report[0]<report[1]):
        for i in range(len(report)-1):
            if int(report[i]) > int(report[i+1]):
                flag +=1
    else:
        for i in range(len(report)-1):
            if int(report[i]) < int(report[i+1]):
                flag +=1
    return flag




flag = 0
for i in arr:
    flagg = 0
    arra = i.split(" ")
    for j in range(len(arra)):
        temp = arra.copy()

        temp.pop(j)
        if(difference(temp) == 0 and direction(temp) == 0):
            pass
        else:
            flagg += 1

    if flagg == len(arra):
        flag += 1
        

print(len(arr) -flag)
        
    # remove the 1 value causing flag in difference and check ascending 





# for every report run a function which checks:
#   1 <= diff <= 3; 1 wrong no could cause 2 error max
#  ascending or descending, first go through each one and determine
# if the array is mostly asc or desc, then check for more  than 1 contridiction