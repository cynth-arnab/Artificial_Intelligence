#visual explanation models
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications import VGG16, imagenet_utils
from tensorflow.keras.models import Model

# Load pre-trained VGG16 model
model = VGG16(weights="imagenet")

# Load and preprocess the image
img = cv2.imread('witcher3.jpg')
img_resize = cv2.resize(img, (224, 224))
plt.imshow(img_resize)

img = load_img("witcher3.jpg", target_size=(224, 224))
img = img_to_array(img)
img = np.expand_dims(img, axis=0)
img = imagenet_utils.preprocess_input(img)
plt.imshow(img[0])

pred = model.predict(img)

# Decode predictions
decod = imagenet_utils.decode_predictions(pred, top=5)
(img_id, label, prob) = decod[0][0]
print(label, ":", prob * 100)

# Construct a new model for gradient computation
gradModel = Model(inputs=model.inputs, outputs=[model.get_layer('block5_conv3').output, model.output])

# Compute gradients
with tf.GradientTape() as tape:
    input = tf.cast(img, tf.float32)
    (convOutputs, predictions) = gradModel(input)
    pred_index = tf.argmax(pred[0])
    loss = predictions[:, pred_index]

grads = tape.gradient(loss, convOutputs)
pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
last_conv_layer_output = convOutputs[0]
saliency_maps = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
saliency_maps = tf.squeeze(saliency_maps)
saliency_maps = tf.maximum(saliency_maps, 0)
tf.reduce_max(saliency_maps)
saliency_maps.numpy()

plt.figure(figsize=(15, 5))
plt.subplot(131)
plt.title('Saliency Map')
plt.imshow(saliency_maps)

plt.subplot(132)
plt.title('Preprocessed Image')
plt.imshow(img[0])

plt.subplot(133)
plt.title('Original Image')
plt.imshow(img_resize)

plt.imshow(img_resize)
plt.show()
