import pandas as pd
data = {
    "Name": ["Ram", "Robert", "Rahim"],
    "Age": [25, 30, 35],
    "City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)

filtered_df = df[df["Age"].isin([35])]
print(filtered_df)