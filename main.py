import requests
import json

def main():
  getCustomerOrder()
  getOrderById('abbigail.kautzer.764458@test.com')

def getCustomerOrder():
  response = requests.get('https://sapstore.conuhacks.io/orders/')
  with open('orderData.json', 'w') as orderData:
    json.dump(response.json(), orderData)

def getOrderById(id):
  URL = 'https://sapstore.conuhacks.io/orders/byEmail?email=' + id
  print(URL)
  response = requests.get(URL)
  print(response)
  with open('orderCache.json', 'w') as orderData:
    json.dump(response.json(), orderData)

if __name__ == "__main__":
  main()