import requests 

# https://git.heroku.com/dgt-class.git
# http://localhost:5000/predict
resp = requests.post("https://dgt-class.herokuapp.com/predict", files={'file': open('eight.png', 'rb')})

print(resp.text)
