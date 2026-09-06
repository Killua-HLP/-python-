year = int(input("Enter th year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is the leap year.") 
elif (year % 4 == 0) and (year % 100 != 0):
    print(f"{year} is the leap year.")
else:
    print(f"{year} is not the leap year.")
    
