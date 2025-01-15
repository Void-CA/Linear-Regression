import pandas as pd

# Cargar los datos
heights = pd.read_csv('data/GaltonFamilies.csv')

# Limpiar los datos
heights = heights.drop(columns=["rownames", "family"])

# Convertir las alturas a centímetros
numerical = ['father', 'mother', 'midparentHeight', 'childHeight']
heights[numerical] = heights[numerical] * 2.54

def get_heights():
    return heights