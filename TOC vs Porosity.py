import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Sample name': ['Shale-01', 'Shale-02', 'Shale-03', 'Shale-04', 'Shale-05', 'Shale-06'],
    'TOC': [0.536, 1.24, 1.88, 0.95, 1.47, 1.59],
    'Porosity (Pore Volume)': [0.062, 0.042, 0.054, 0.057, 0.035, 0.069],
    'Porosity (Surface Area)': [26.131, 11.081, 15.041, 21.937, 10.143, 40.005]
}

df = pd.DataFrame(data)

# Filter out Shale-06
df_filtered = df[df['Sample name'] != 'Shale-06']

# Calculate correlations excluding Shale-06
r_pore_volume = df_filtered['TOC'].corr(df_filtered['Porosity (Pore Volume)'])
r_surface_area = df_filtered['TOC'].corr(df_filtered['Porosity (Surface Area)'])

# Calculate r²
r2_pore_volume = r_pore_volume**2
r2_surface_area = r_surface_area**2

# --- Plotting ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot 1: Porosity (Pore Volume) vs TOC
axes[0].scatter(df['TOC'], df['Porosity (Pore Volume)'], color='blue', s=100)
axes[0].set_title('Porosity (Pore Volume)', fontsize=20)
axes[0].set_xlabel('Total Organic Carbon (TOC) (%)', fontsize=20)
axes[0].set_ylabel('Pore Volume (cm$^3$/g)', fontsize=20)
axes[0].tick_params(axis='y', labelsize=16)
axes[0].tick_params(axis='x', labelsize=16)
axes[0].set_xlim(0.4, 2.0)
axes[0].set_ylim(0.03, 0.075)

# Annotate sample names
for i, txt in enumerate(df['Sample name']):
    color = 'red' if txt == 'Shale-06' else 'black'
    axes[0].annotate(
        txt, 
        (df['TOC'][i], df['Porosity (Pore Volume)'][i]), 
        textcoords="offset points", 
        xytext=(0,10), 
        ha='center', 
        fontsize=14, 
        color=color
    )

# Add r and r² values
axes[0].text(
    0.99, 0.99, 
    f"r = {r_pore_volume:.2f}\nr² = {r2_pore_volume:.2f}", 
    fontsize=16, color="black", 
    ha='right', va='top', transform=axes[0].transAxes
)

# Plot 2: Porosity (Surface Area) vs TOC
axes[1].scatter(df['TOC'], df['Porosity (Surface Area)'], color='red', s=100)
axes[1].set_title('Porosity (Surface Area)', fontsize=20)
axes[1].set_xlabel('Total Organic Carbon (TOC) (%)', fontsize=20)
axes[1].set_ylabel('Pore Surface Area (m$^2$/g)', fontsize=20)
axes[1].tick_params(axis='y', labelsize=16)
axes[1].tick_params(axis='x', labelsize=16)
axes[1].set_xlim(0.4, 2.0)
axes[1].set_ylim(5, 45)

# Annotate sample names
for i, txt in enumerate(df['Sample name']):
    color = 'red' if txt == 'Shale-06' else 'black'
    axes[1].annotate(
        txt, 
        (df['TOC'][i], df['Porosity (Surface Area)'][i]), 
        textcoords="offset points", 
        xytext=(0,10), 
        ha='center', 
        fontsize=14, 
        color=color
    )

# Add r and r² values
axes[1].text(
    0.99, 0.99, 
    f"r = {r_surface_area:.2f}\nr² = {r2_surface_area:.2f}", 
    fontsize=16, color="black", 
    ha='right', va='top', transform=axes[1].transAxes
)

plt.tight_layout()
plt.show()
