year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year")
    print("This year is centry year")
    print("century year is detected")
    print("Timmu")
else:
    print(year, "is not a leap year")
     print("This year is not centry year")
       print("century year is not detected")


