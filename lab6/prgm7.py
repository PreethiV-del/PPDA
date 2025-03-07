import pandas as pd
data = {
    "Name": ["Ram", "Robert", "Rahim"],
    "Age": [25, 30, 35],
    "City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)

filtered_df = df[df["Age"] > 25]
print(filtered_df)
