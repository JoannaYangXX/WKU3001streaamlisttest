# This program determine wether You will accept loan application or reject based on annual salary and year of work .annual dalary >= 50,000 and work year >=5.You haveto tell them how much salary or year of work or salary and year of work need more when you reject


criteria_annual_salary = 50000  
criteria_year_work = 5  

annual_salary = float(input("Enter your annual salary (in yuan): "))
year_work = int(input("Enter your total years of work: "))

if annual_salary >= criteria_annual_salary:
    if year_work >= criteria_year_work:
        print("Accept: Your loan application is approved.")
    else:
        need_year = criteria_year_work - year_work
        print(f"Rejected: You need {need_year} more years of work experience.")
else:
    need_salary = criteria_annual_salary - annual_salary
    need_year = criteria_year_work - year_work

   
    if need_salary > 0 and need_year > 0:
        print(f"Rejected: You need an additional {need_salary:.2f} yuan in salary and {need_year} more years of work experience.")
    elif need_salary > 0:
        print(f"Rejected: You need an additional {need_salary:.2f} yuan in salary.")
    elif need_year > 0:
        print(f"Rejected: You need {need_year} more years of work experience.")