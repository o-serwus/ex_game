month = input("State your month: ")

if(month.lower() == "january", "march", "may", "july", "august", "october", "december"):
    print("Input the name of Month", month)
    print("Number of days: 31 days")
elif(month.lower() == "april", "june", "september", "november"):
    print("Input the name of Month", month)
    print("Number of days: 30 days")
else:
    print("Input the name of Month", month)
    print("Number of days: 28/29 days") 