import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load Data
df = pd.read_csv("datasetKS2.csv")
df['yield_kg_ha'] = df['produksi'] / df['luas_ha']
subset = df[[
    'populasi_ha',
    'sex_ratio',
    'yield_kg_ha'
]]

X = df[['populasi_ha','sex_ratio']]
y = df['yield_kg_ha']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
data_baru = pd.DataFrame({
    'populasi_ha':[143],
    'sex_ratio':[0.70]
})
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='green', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--', lw=2)  # garis ideal
plt.xlabel('Yield Actual (kg/ha)')
plt.ylabel('Yield Prediction (kg/ha)')
plt.title(f'Prediction vs Actual\nMSE={mse:.2f}, R²={r2:.3f}')
plt.grid(True)
plt.show()