import pandas as pd

# Load your dataset
dataset_path = "/Users/mac/Desktop/apk/apk_ml_model/CSV/malgenome-215.csv"
df = pd.read_csv(dataset_path)
# Shuffle the rows randomly
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled dataset to a new CSV file (or overwrite the original)
df_shuffled.to_csv("malgenome-215_shuffled.csv", index=False)

print("Dataset shuffled and saved to 'your_dataset_shuffled.csv'")
