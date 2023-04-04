import json

data = {
  "Andhra Pradesh": "Amaravati",
  "Bihar": "Patna",
  "Gujarat": "Gandhinagar",
  "Karnataka": "Bengaluru",
  "Maharashtra": "Mumbai",
  "Punjab": "Chandigarh",
  "Tamil Nadu": "Chennai"
}

with open('state.json','w')as f:
    json.dump(data,f)