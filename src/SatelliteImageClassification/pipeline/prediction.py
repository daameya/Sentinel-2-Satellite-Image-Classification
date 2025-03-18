import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("model", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64,64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 1:
            prediction = 'AnnualCrop'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = "Forest"
            return [{"image" : prediction}]
        elif result[0] == 3:
            prediction = "HerbaceousVegetation"
            return [{"image" : prediction}]
        elif result[0] == 4:
            prediction = "Highway"
            return [{"image" : prediction}]
        elif result[0] == 5:
            prediction = "Industrial"
            return [{"image" : prediction}]
        elif result[0] == 6:
            prediction = "Pasture"
            return [{"image" : prediction}]
        elif result[0] == 7:
            prediction = "PermanentCrop"
            return [{"image" : prediction}]
        elif result[0] == 8:
            prediction = "Residential"
            return [{"image" : prediction}]
        elif result[0] == 9:
            prediction = "River"
            return [{"image" : prediction}]
        else:
            prediction = 'SeaLake'
            return [{ "image" : prediction}]