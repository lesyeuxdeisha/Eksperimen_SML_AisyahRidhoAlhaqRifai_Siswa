import pandas as pd
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Menggunakan autolog (Syarat Basic)
mlflow.autolog()

# Pastikan baris ini menggunakan 'heart_disease_preprocessing'
df = pd.read_csv('heart_disease_preprocessing/heart_disease_clean.csv')
X = df.drop('num', axis=1)
y = df['num']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

with mlflow.start_run(run_name="Basic_Run"):
    model = RandomForestClassifier() # Tanpa tuning (Syarat Basic)
    model.fit(X_train, y_train)