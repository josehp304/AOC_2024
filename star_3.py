with open("reports.txt",'r') as file:
    data = file.read()
# data = """45 52 53 55 55
# 51 53 54 55 57 60 63 63
# 87 90 93 94 98
# 71 73 74 74 75 76 77"""

singleLines = data.split("\n")

intListLines = [list([int(num) for num in item.split(" ")]) for item in singleLines]
safe_reports = 0

for i in range(len(intListLines)):
    direction_arr=[]
    count = 0
    for n in range(len(intListLines[i])-1):
        bool = True
        if abs(intListLines[i][n] - intListLines[i][n+1]) > 3 or abs(intListLines[i][n]- intListLines[i][n+1]) <=0:
            # print(abs(intListLines[i][n] - intListLines[i][n+1]))
            bool = False
            count+=1
            

        if bool and intListLines[i][n] < intListLines[i][n+1]:
            # print(intListLines[i][n], intListLines[i][n+1])
            direction_arr.append(1)
        elif bool and intListLines[i][n] > intListLines[i][n+1]:
            direction_arr.append(0)

    if 0<direction_arr.count(0)and direction_arr.count(0)!=len(direction_arr):
        # print(intListLines[i])
        count+= min(direction_arr.count(0),direction_arr.count(1))
    # if count==1:print(intListLines[i],direction_arr , count )
    if count<=1:
        safe_reports+=1
print(safe_reports)
# for i in range(len(intListLines)):
#     direction = None
#     count = 0
#     for n in range(len(intListLines[i])):
        
        
#         if n ==0:
#             if intListLines[i][n] < intListLines[i][n+1]:
#                 direction = 'asc'
#             elif intListLines[i][n] > intListLines[i][n+1]:
#                 direction = 'dsc'
#             else:
                
#                 count +=1
#         if n !=0:
#             if direction=='asc' and intListLines[i][n] > intListLines[i][n-1] and 0 < intListLines[i][n] - intListLines[i][n-1] <4:
                
#                 count +=0
#             elif(direction=='dsc' and intListLines[i][n] < intListLines[i][n-1] and 0 < intListLines[i][n-1] - intListLines[i][n] <4):

#                 count +=0
                
#             else:
#                 # print("eliminated")
#                 count +=1
                
    




# for star 4 
#after every eleimination add one to the count  
# instead of breaking check how many elimination happend in the list and if the elimination is less than one 
# check asc or dsc from the first two vaiable and if all the other num are in oppostie direction to 1st num then make it true
# total number of nums -2 <= no of elimination then removing the first element will make it true 