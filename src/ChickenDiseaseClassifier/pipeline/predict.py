import numpy as np
import tensorflow as tf
import os

class PredictionPipeline:
    def __init__(self,filename):
        self.filename=filename
        
    def predict(self):
        # load model
        model = tf.keras.models.load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = tf.keras.preprocessing.image.load_img(imagename, target_size = (224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'Healthy'
            return [{ "image" : prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{ "image" : prediction}]
        