year = int(input("Enter year: "))

print(f"{year} is {"not" if(not (((year % 100 == 0) and (year % 400 == 0)) or ((year % 100 != 0) and (year % 4 == 0)))) else ""} a leap year")