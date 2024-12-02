with open("reports.txt",'r') as file:
    data = file.read()
# data = """27 29 30 33 34 35 37 35
# 51 53 54 55 57 60 63 63
# 87 90 93 94 98
# 41 42 45 47 49 51 53 58
# 23 26 23 24 27 28
# 32 33 36 37 34 36 39 37
# 12 13 11 14 14
# 84 87 88 87 91
# 54 55 53 56 62
# 71 73 74 74 75 76 77"""

singleLines = data.split("\n")

intListLines = [list([int(num) for num in item.split(" ")]) for item in singleLines]
safe_reports = 0
for i in range(len(intListLines)):
    direction = None
    check = True

    for n in range(len(intListLines[i])):

        
        if n ==0:
            if intListLines[i][n] < intListLines[i][n+1]:
                direction = 'asc'
            elif intListLines[i][n] > intListLines[i][n+1]:
                direction = 'dsc'
            else:
                check = False
                break
        if n !=0:
            if direction=='asc' and intListLines[i][n] > intListLines[i][n-1] and 0 < intListLines[i][n] - intListLines[i][n-1] <4:
                
                check = True
            elif(direction=='dsc' and intListLines[i][n] < intListLines[i][n-1] and 0 < intListLines[i][n-1] - intListLines[i][n] <4):

                check=True
            else:
                print("eliminated")
                check=False
                break
    
    if check == True:
        safe_reports +=1



    # go through each number in the list 
    # check if second num is greater than or less than first num and set the asc or dec accordingly
    # check if the other follow asc or des 
    # check if the difference btw previous num and current num is 0 < num > 3
    # if any of the rules is violated break the loop right there
    # else add 1 to safe_reports 

print(safe_reports)