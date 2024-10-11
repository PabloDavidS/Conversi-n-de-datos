# Importar os para manipular rutas de archivos y directorios
# Importar pd para trabajar con DataFrames 
import os
import pandas as pd

# Directorio que contiene las carpetas de imágenes
data_dir = r"C:\Users\Pablo\Documents\trabajo de grado\TINTOlib\img-analisis1"

# Lista para almacenar las rutas de las imágenes y sus etiquetas
ruta_img = []
carpetas = []

# ciclo for para iterar en las carpetas creadas por la libreria
for nom_carp in os.listdir(data_dir):
    # con el siguiente metodo unirmeos la ruta (data_dir) con (dir_carp) para formar la ruta especifica a los archivos de cada carpeta creada
    dir_carp = os.path.join(data_dir, nom_carp)
    #verifica que la ruta exista
    if os.path.isdir(dir_carp):
        # ciclo for para iterar en las imagenes de cada carpeta
        for nom_img in os.listdir(dir_carp):
            # unimos la direccion que tenemos en (dir_carp) con (nom_img) para crear la direccion exacta de la imagen 
            dir_img = os.path.join(dir_carp,nom_img)
            #guardamos en el vector (ruta_img) la direccion de la carpeta
            ruta_img.append(dir_img)
            #guardamos en el vector (carpetas) el nombre de la carpeta
            carpetas.append(nom_carp)
#crear un DataFrame con las direcciones de las imagenes y las carpetas a las que pertenecen 
df = pd.DataFrame({"ruta_imagen": ruta_img, "carpeta": carpetas})



# Importamos (train_test_split) que nos permite dividir los datos en subconjuntos de entrenamiento, calidacion y prueba 
from sklearn.model_selection import train_test_split

# División de características y etiquetas
X = df["ruta_imagen"]
Y = df["carpeta"] 

# División de conjunto de entrenamiento (70% de los datos) y conjunto de datos de prueba (30% de los datos)
# (X_train, y_train) conjunto de entrenamiento - (X_test, y_test) conjunto de prueba 
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# División del conjunto de entrenamiento (70% dts) en conjunto de entrenamiento y validacion 
#(X_val, y_val) conjunto de validacion 40% - (X_train, y_train)conjunto de entrenamiento 60%
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.4, random_state=42)

# Concatenación de características y etiquetas para cada conjunto
# Se concatenan las características y las etiquetas correspondientes para formar DataFrames separados para cada conjunto: entrenamiento, prueba y validación
df_train = pd.concat([X_train, y_train], axis=1)
df_test = pd.concat([X_test, y_test], axis=1)
df_val = pd.concat([X_val, y_val], axis=1)

# Convertir los valores en la columna "carpeta" a cadenas, necesario para el codigo de cambiar tamaño de imagenes
df_train['carpeta'] = df_train['carpeta'].astype(str)
df_val['carpeta'] = df_val['carpeta'].astype(str)
df_test['carpeta'] = df_test['carpeta'].astype(str)


# Guardar DataFrames en archivos CSV
df_train.to_csv('df_train.csv', index=False)
df_val.to_csv('df_val.csv', index=False)
df_test.to_csv('df_test.csv', index=False)
print("codigo ejecutado")
