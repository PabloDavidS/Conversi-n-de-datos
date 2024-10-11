# Importamos la clase ImageDataGenerator de Keras, útil para realizar preprocesamiento de imágenes y aumentar el tamaño del conjunto de datos
from keras.preprocessing.image import ImageDataGenerator

# Definir generadores de datos
# Creamos generadores de datos para los conjuntos de entrenamiento, validación y prueba
# El parámetro rescale=1./255 normaliza los valores de los píxeles a un rango de 0 a 1
train_datagen = ImageDataGenerator(rescale=1./255)
valid_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Define el tamaño al que se redimensionarán todas las imágenes. Aquí se usa 224x224 píxeles
pixels = 224  

# Crear iteradores de datos
train_iter = train_datagen.flow_from_dataframe(
    df_train,
    target_size=(pixels, pixels),
    x_col='image_path',  # Asegúrate de que este nombre coincida con la columna en tu DataFrame
    y_col='label',  # Asegúrate de que este nombre coincida con la columna en tu DataFrame
    class_mode='categorical',
    color_mode='rgb',
    batch_size=8,
    shuffle=True
)

valid_iter = valid_datagen.flow_from_dataframe(
    df_val,
    target_size=(pixels, pixels),
    x_col='image_path',
    y_col='label',
    class_mode='categorical',
    color_mode='rgb',
    batch_size=8,
    shuffle=False
)

test_iter = test_datagen.flow_from_dataframe(
    df_test,
    target_size=(pixels, pixels),
    x_col='image_path',
    y_col='label',
    class_mode='categorical',
    color_mode='rgb',
    batch_size=8,
    shuffle=False
)

# Verifica el tamaño de las imágenes
print(next(train_iter)[0].shape)  # Obtenemos un lote de imágenes del iterador y mostramos su forma
print(next(valid_iter)[0].shape)
print(next(test_iter)[0].shape)

