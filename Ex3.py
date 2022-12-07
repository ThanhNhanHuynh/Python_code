NumberList = []

def get_num_input():
    n = int(input('Enter number of elements: '))
    for e in range(0, n):
        e = int(input())
        NumberList.append(e)
    print(NumberList)
    
def find_max_min():
    max = min = NumberList[0]
    for i in NumberList:
        if i > max:
            max = i
    print("Max =",max)       
    for i in NumberList:
        if i < min:
            min = i
    print("Min =",min)

get_num_input()
find_max_min()