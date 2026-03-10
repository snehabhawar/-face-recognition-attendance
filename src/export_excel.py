import pandas as pd

# Read CSV attendance
df = pd.read_csv("../attendance/attendance.csv")

# Save as Excel
excel_file = "../attendance/attendance.xlsx"

df.to_excel(excel_file, index=False)

print("Excel attendance sheet created:", excel_file)