# Rent4You - Datos Preprocesados

Este repositorio contiene los **datos preprocesados** del caso de estudio *Rent4You* para la materia **Extracción de conocimiento en bases de datos**.

## Objetivo
Preparar los datos de **ventas por sucursal** para su posterior análisis en el Data Warehouse.

## Archivos
- `data/ventas.csv`: datos originales de ventas
- `data/sucursales.csv`: catálogo de sucursales
- `data/ventas_preprocesadas.csv`: datos limpios y consolidados
- `scripts/preprocesamiento_ventas.py`: script ETL en Python (Pandas)

##  Procesos aplicados
- Eliminación de filas vacías  
- Validación de valores numéricos  
- Conversión de fechas a formato estándar  
- Cálculo de margen bruto  
- Integración con tabla de sucursales  

## Herramientas
- Python 3.x  
- Pandas  

## Autor
Wensley Pierre  
Universidad Tecnológica de Querétaro  
Materia: Extracción de conocimiento en bases de datos  
Profesor: Filiberto Ruiz Hernández
