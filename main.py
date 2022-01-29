import requests
import json

def main():
  getCustomerOrder()
  #getOrderById('abbigail.kautzer.764458@test.com')

def getCustomerOrder():
  response = requests.get('https://sapstore.conuhacks.io/orders/')
  with open('orderData.json', 'w') as orderData:
    json.dump(response.json(), orderData)

def getOrderByEmail(email):
  URL = 'https://sapstore.conuhacks.io/orders/byEmail?email=' + email
  response = requests.get(URL)
  with open('orderCache.json', 'w') as orderData:
    json.dump(response.json(), orderData)

def getOrderByID(id):
  URL = 'https://sapstore.conuhacks.io/orders/' + id
  response = requests.get(URL)
  with open('orderCache.json', 'w') as orderData:
    json.dump(response.json(), orderData)

if __name__ == "__main__":
  main()