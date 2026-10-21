# solution 1

def cm_to_feet_and_inches(cm):
    total_inch = cm * 0.393701
    feet = int(total_inch // 12)
    inch = round(total_inch % 12, 1)
    
    return f"{feet} feet and {inch} inches"


cm = int(input("Enter value in cm: "))
print(cm_to_feet_and_inches(cm))







# solution 2

n = int(input("Enter number: "))
def total_sum(n):
    if(n==1):
        return 1
    return n + total_sum(n-1)


print(total_sum(n))
