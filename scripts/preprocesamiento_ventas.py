import pandas as pd

# Cargar datos
ventas = pd.read_csv('../data/ventas.csv')
sucursales = pd.read_csv('../data/sucursales.csv')

# Limpieza básica
ventas.dropna(inplace=True)
ventas = ventas[ventas['total_pagado'] > 0]
ventas['fecha'] = pd.to_datetime(ventas['fecha'])

# Calcular margen bruto
ventas['margen_bruto'] = ventas['total_pagado'] - (ventas['tarifa_base'] * 0.75)

# Unir con sucursales
ventas_sucursal = ventas.merge(sucursales, on='sucursal_id', how='left')

# Guardar archivo final
ventas_sucursal.to_csv('../data/ventas_preprocesadas.csv', index=False)
print("✅ Archivo 'ventas_preprocesadas.csv' generado correctamente.")
