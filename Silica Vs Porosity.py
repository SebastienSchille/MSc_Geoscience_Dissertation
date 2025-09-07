import pandas as pd
import matplotlib.pyplot as plt

# Data (Silica Content from your image)
data = {
    'Sample name': ['Shale-01', 'Shale-02', 'Shale-03', 'Shale-04', 'Shale-05', 'Shale-06'],
    'Silica Content (wt%)': [60.5, 61.4, 49.0, 54.0, 29.9, 53.9],
    'Porosity (Pore Volume)': [0.062, 0.042, 0.054, 0.057, 0.035, 0.069],
    'Porosity (Surface Area)': [26.131, 11.081, 15.041, 21.937, 10.143, 40.005]
}

df = pd.DataFrame(data)

# --- Correlations excluding only Shale-06 (for plotting) ---
df_excl_06 = df[df['Sample name'] != 'Shale-06']

# Correlations for plotting
r_pore_volume_excl_06 = df_excl_06['Silica Content (wt%)'].corr(df_excl_06['Porosity (Pore Volume)'])
r2_pore_volume_excl_06 = r_pore_volume_excl_06 ** 2

r_surface_area_excl_06 = df_excl_06['Silica Content (wt%)'].corr(df_excl_06['Porosity (Surface Area)'])
r2_surface_area_excl_06 = r_surface_area_excl_06 ** 2

# --- Correlations excluding Shale-06 and Shale-02 (for printing only) ---
df_excl_06_02 = df[~df['Sample name'].isin(['Shale-06', 'Shale-02'])]

r_pore_volume_excl_06_02 = df_excl_06_02['Silica Content (wt%)'].corr(df_excl_06_02['Porosity (Pore Volume)'])
r2_pore_volume_excl_06_02 = r_pore_volume_excl_06_02 ** 2

r_surface_area_excl_06_02 = df_excl_06_02['Silica Content (wt%)'].corr(df_excl_06_02['Porosity (Surface Area)'])
r2_surface_area_excl_06_02 = r_surface_area_excl_06_02 ** 2

# Print the correlations excluding Shale-06 and Shale-02
print("Excluding Shale-06 and Shale-02:")
print(f"Pore Volume: r = {r_pore_volume_excl_06_02:.2f}, R² = {r2_pore_volume_excl_06_02:.2f}")
print(f"Surface Area: r = {r_surface_area_excl_06_02:.2f}, R² = {r2_surface_area_excl_06_02:.2f}")

# --- Plotting ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Porosity (Pore Volume) vs Silica
axes[0].scatter(df['Silica Content (wt%)'], df['Porosity (Pore Volume)'], color='blue', s=100)
axes[0].set_title('Porosity (Pore Volume)', fontsize=20)
axes[0].set_xlabel('Silica Content (wt%)', fontsize=20)
axes[0].set_ylabel('Pore Volume (cm$^3$/g)', fontsize=20)
axes[0].set_xlim(25, 65)
axes[0].set_ylim(0.03, 0.075)
axes[0].tick_params(axis='y', labelsize=16)
axes[0].tick_params(axis='x', labelsize=16)

# Annotate all sample names
for i, txt in enumerate(df['Sample name']):
    color = 'red' if txt == 'Shale-06' else 'black'
    axes[0].annotate(
        txt,
        (df['Silica Content (wt%)'][i], df['Porosity (Pore Volume)'][i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center',
        va='bottom',
        fontsize=14,
        color=color
    )

# Add r and R² values (top-right)
axes[0].text(
    0.97, 0.97, 
    f"r = {r_pore_volume_excl_06:.2f}\nR² = {r2_pore_volume_excl_06:.2f}", 
    fontsize=14, color="black", 
    ha='right', va='top', transform=axes[0].transAxes
)

# Plot 2: Porosity (Surface Area) vs Silica
axes[1].scatter(df['Silica Content (wt%)'], df['Porosity (Surface Area)'], color='red', s=100)
axes[1].set_title('Porosity (Surface Area)', fontsize=20)
axes[1].set_xlabel('Silica Content (wt%)', fontsize=20)
axes[1].set_ylabel('Pore Surface Area (m$^2$/g)', fontsize=20)
axes[1].set_xlim(25, 65)
axes[1].set_ylim(5, 45)
axes[1].tick_params(axis='y', labelsize=16)
axes[1].tick_params(axis='x', labelsize=16)

# Annotate all sample names
for i, txt in enumerate(df['Sample name']):
    color = 'red' if txt == 'Shale-06' else 'black'
    axes[1].annotate(
        txt,
        (df['Silica Content (wt%)'][i], df['Porosity (Surface Area)'][i]),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center',
        va='bottom',
        fontsize=14,
        color=color
    )

# Add r and R² values (top-right)
axes[1].text(
    0.97, 0.97, 
    f"r = {r_surface_area_excl_06:.2f}\nR² = {r2_surface_area_excl_06:.2f}", 
    fontsize=14, color="black", 
    ha='right', va='top', transform=axes[1].transAxes
)

plt.tight_layout()
plt.show()
