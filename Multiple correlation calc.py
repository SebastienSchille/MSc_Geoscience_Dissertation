import pandas as pd
import numpy as np

# Load the combined data into a pandas DataFrame.
data = {
    'Sample_name': ['Shale-01', 'Shale-02', 'Shale-03', 'Shale-04', 'Shale-05'],
    'TOC': [0.536, 1.24, 1.88, 0.95, 1.47],
    'Thermal_Maturity': [1.4, 1.25, 1.2, 1.2, 0.9],
    'Silica_Content': [60.5, 61.4, 49.0, 54.0, 29.9],
    'Porosity_Pore_Volume': [0.062, 0.042, 0.054, 0.057, 0.035],
    'Porosity_Surface_Area': [26.131, 11.081, 15.041, 21.937, 10.143],
    'Porosity_%': [16.8, 11.5, 14.6, 15.5, 9.5]
}

df = pd.DataFrame(data)

def calculate_multiple_r(Y, X):
    X_matrix = np.c_[np.ones(X.shape[0]), X]
    beta = np.linalg.inv(np.dot(X_matrix.T, X_matrix)).dot(X_matrix.T).dot(Y)
    Y_hat = np.dot(X_matrix, beta)
    SS_tot = np.sum((Y - np.mean(Y)) ** 2)
    SS_res = np.sum((Y - Y_hat) ** 2)
    R_squared = 1 - (SS_res / SS_tot)
    R = np.sqrt(R_squared)
    return R, R_squared

# --- Calculation 1: Dependent Variable = Porosity (Pore Volume) ---
print("--- Calculating for Dependent Variable: Porosity (Pore Volume) ---")
Y_pv = df['Porosity_Pore_Volume']
X = df[['TOC', 'Thermal_Maturity', 'Silica_Content']]
r_pv, r_squared_pv = calculate_multiple_r(Y_pv, X)
print(f"R-squared: {r_squared_pv:.4f}")
print(f"Multiple Correlation Coefficient (R): {r_pv:.4f}")
print("-" * 50)

# --- Calculation 2: Dependent Variable = Porosity (Surface Area) ---
print("\n--- Calculating for Dependent Variable: Porosity (Surface Area) ---")
Y_sa = df['Porosity_Surface_Area']
r_sa, r_squared_sa = calculate_multiple_r(Y_sa, X)
print(f"R-squared: {r_squared_sa:.4f}")
print(f"Multiple Correlation Coefficient (R): {r_sa:.4f}")
print("-" * 50)

# --- Calculation 3: Dependent Variable = Porosity (%) ---
print("\n--- Calculating for Dependent Variable: Porosity (%) ---")
Y_pct = df['Porosity_%']
r_pct, r_squared_pct = calculate_multiple_r(Y_pct, X)
print(f"R-squared: {r_squared_pct:.4f}")
print(f"Multiple Correlation Coefficient (R): {r_pct:.4f}")
print("-" * 50)

# --- Correlation between Thermal Maturity and TOC ---
correlation = df['Thermal_Maturity'].corr(df['TOC'])
r_squared_tm_toc = correlation ** 2
print("\n--- Correlation between Thermal Maturity and TOC ---")
print(f"Pearson correlation: {correlation:.4f}")
print(f"R-squared: {r_squared_tm_toc:.4f}")
