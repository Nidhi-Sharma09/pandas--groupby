import pandas as pd
data = {
    "Employee": ["Aman", "Rahul", "Priya", "Neha", "Vikas", "Sneha"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 42000, 55000]
}
df = pd.DataFrame(data)


'''basic group by'''
#Find the total salary paid by each department.
print("sum: ")
print(df.groupby("Department")["Salary"].sum())

#Average salary of each department
print("\navg: ")
print(df.groupby("Department")["Salary"].mean())

#Highest salary of each department
print("\nhigest: ")
print(df.groupby("Department")["Salary"].max())

#Lowest salary of each department
print("\nlowest: ")
print(df.groupby("Department")["Salary"].min())

#⭐ Number of employees in each department
print("\nnumber of employee in each:")
print(df.groupby("Department")["Employee"].count()) 



'''agg()'''
#example:
print(df.groupby("Department")["Salary"].agg(
    ["mean","max","min","count"]
    )
)

#example:
print(
    df.groupby("Department").agg({
        "Salary": ["mean", "max", "min"],
        "Employee": "count"
    })
)
