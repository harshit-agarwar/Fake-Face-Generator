#---DEPENDENCIES--------------------------------------------------------------+

#---general
import numpy as np

#---tensorflow
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

#---GENERATE FAKE FACES-------------------------------------------------------+
gen = load_model('./generator.h5')

def gene():
    noise = np.random.normal(0, 1, (1, 100))
    gen_imgs = gen.predict(noise)
    gen_imgs = np.reshape(gen_imgs,(28,28,3))
    a = image.array_to_img(gen_imgs)
    return a

