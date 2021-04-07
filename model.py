import numpy as np
import tensorflow as tf
from tensorflow import keras


model = keral.models.load_model('senior_forever.ipynb')

with open('searches.json') as json_file:
    data = json.load(json_file)

np.testing.assert_allclose(model.predict(data['current']['bedrooms'], data['current']['bathrooms'], data['current']['floors'], data['current']['sqft']))

# test_data = np.array([5,    2.50,   2910,   1.0])
 
# print(model.predict(test_data.reshape(1,4), batch_size=1))