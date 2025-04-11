import pandas as pd
employees = pd.DataFrame({
"emp_id": [1, 2, 3],
"dept_id": [101, 102, 103],
"product": ["A", "B", "A"]
})
departments = pd.DataFrame({
"dept_id": [101, 102, 104],
"dept_name": ["HR", "Engg", "Mkt"],
"product": ["A", "B", "C"]
})
left_merged = pd.merge(employees, departments, on="dept_id", how="left")
print("Left join:\n", left_merged)
