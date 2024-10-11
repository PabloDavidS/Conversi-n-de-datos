from TINTOlib.barGraph import BarGraph

# Configuración de parámetros del modelo (ajustar según sea necesario)
model = BarGraph(problem='supervised')


# Especificar la ruta del archivo CSV con los datos (incluyendo la extensión .CSV)
csv_path = r"C:/Users/Pablo/Documents/trabajo de grado/TINTOlib/Prueba 1 - TINTO/primer-analisis.CSV"

# Especificar la carpeta donde se guardarán las imágenes generadas
result_folder_path = r"C:/Users/Pablo/Documents/trabajo de grado/TINTOlib/Prueba 4 - BarGraph"

# Generar imágenes a partir de los datos
model.generateImages(csv_path, result_folder_path)