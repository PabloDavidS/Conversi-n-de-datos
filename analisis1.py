# Importa TINTOlib para la generación de imágenes a partir de datos tabulares
from TINTOlib.tinto import TINTO
# Crear una instancia del modelo TINTO
model = TINTO()
# configuracion de parametros del modelo
model = TINTO(algorithm="t-SNE",pixels=30,blur=True,option="maximum")
# Especificar la ruta del archivo CSV con los datos (incluyendo la extensión .CSV)
csv_path = r"C:\Users\Pablo\Documents\trabajo de grado\TINTOlib\primer-analisis.CSV"
# Especificar la carpeta donde se guardarán las imágenes generadas
result_folder_path = r"C:\Users\Pablo\Documents\trabajo de grado\TINTOlib\img-analisis1"
# Generar imágenes a partir de los datos
model.generateImages(csv_path, result_folder_path)
