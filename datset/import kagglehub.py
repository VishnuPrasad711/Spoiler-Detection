import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("rmisra/imdb-spoiler-dataset")
print("Path to dataset files:", path)

# Load the reviews file into a DataFrame (was missing before - caused NameError)
df = pd.read_json(os.path.join(path, "IMDB_reviews.json"), lines=True)
print("First 5 records:", df.head())