import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import imagenet_utils

# Carregar o modelo pré-treinado
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Função para realizar a classificação
def classify_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))  # Redimensionar a imagem para o tamanho esperado pelo modelo
    img = image.img_to_array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)  # Pré-processar a imagem
    img = tf.expand_dims(img, axis=0)

    # Fazer a previsão usando o modelo
    predictions = model.predict(img)
    results = imagenet_utils.decode_predictions(predictions, top=3)[0]  # Decodificar as previsões em rótulos

    # Exibir os resultados
    print("Resultados da classificação:")
    for result in results:
        print(f"{result[1]}: {result[2] * 100}%")

# Caminho da imagem que você deseja classificar
image_path = "caminho/para/sua/imagem.jpg"

# Classificar a imagem
classify_image(image_path)