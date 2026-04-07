from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.seasonal import seasonal_decompose

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"Akurasi (R2 Score): {r2:.2f}")
print(f"Kesalahan (MSE): {mse:.2f}")

# Visualitation MSE & R²
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color='green', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--', lw=2)  # garis ideal
plt.xlabel('Yield Actual (kg/ha)')
plt.ylabel('Yield Prediction (kg/ha)')
plt.title(f'Prediction vs Actual\nMSE={mse:.2f}, R²={r2:.3f}')
plt.grid(True)
plt.show()