import json
from fastapi.encoders import jsonable_encoder


# Example object (dictionary in this case)
data_dict = "{\"captureDate\":\"2022-02-23T09:15:09.481Z\",\"observationText\":\"\",\"savedTagList\":[],\"cameraOrientation\":\"NA\",\"fileLat\":\"28.6381098\",\"fileLng\":\"77.0505793\"}"
# Convert the dictionary to a JSON-formatted string

imageJson = json.dumps(jsonable_encoder(data_dict))
imageJson1 = json.dumps(jsonable_encoder(imageJson))
imageJson2 = json.dumps(jsonable_encoder(imageJson1))
# Print the resulting JSON string
print(imageJson1)
