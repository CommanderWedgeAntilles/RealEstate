import numpy as np
import tensorflow as tf
from tensorflow import keras
import json


model = keras.models.load_model('model')

with open('searches.json') as json_file:
    data = json.load(json_file)

#np.testing.assert_allclose(model.predict((data['current']['bedrooms'], data['current']['bathrooms'], data['current']['floors'], data['current']['sqft']), batch_size=1))

test_data = np.array([data['current']['bedrooms'], data['current']['bathrooms'], data['current']['floors'], data['current']['sqft']])
 
propVal = (model.predict(test_data.reshape(1,4), batch_size=1))
print(propVal)


mortgage = propVal*0.4
#loan estimate (30 year 3.25% rate)
yearLoan = ((mortgage*0.0325)*12)
#tax estimate (0.930%)
yearTax = (propVal*0.00930)
#total cost estimate (add closing cost (0.035))
closing = (propVal*0.035)
annualTotal = yearLoan + yearTax + closing

print(annualTotal)

json_config = model.to_json()
new_model = keras.models.model_from_json(json_config)