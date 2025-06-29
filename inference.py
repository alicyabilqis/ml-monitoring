import requests

data = {"example": "test"}
res = requests.post("http://localhost:5000/infer", json=data)
print(res.json())
