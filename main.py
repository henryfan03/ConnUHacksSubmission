import requests
import json

def main():
  getCustomerOrder()
  getOrderByEmail('abbigail.kautzer.764458@test.com')
  localdata = getFromJSON("orderCache.json")
  print(localdata['orderId'])

def getCustomerOrder():
  response = requests.get('https://sapstore.conuhacks.io/orders/')
  with open('orderData.json', 'w') as orderData:
    json.dump(response.json(), orderData)

def getOrderByEmail(email):
  URL = 'https://sapstore.conuhacks.io/orders/byEmail?email=' + email
  response = requests.get(URL)
  with open('orderCache.json', 'w') as orderData:
    json.dump(response.json()[0], orderData)

def getOrderById(id):
  URL = 'https://sapstore.conuhacks.io/orders/' + id
  response = requests.get(URL)
  with open('orderCache.json', 'w') as orderData:
    json.dump(response.json()[0], orderData)

def getStores():
  response = requests.get('https://sapstore.conuhacks.io/stores')
  with open('storeData.json', 'w') as storeData:
    json.dump(response.json(), storeData)

def getStoreById(id):
  URL = 'https://sapstore.conuhacks.io/stores/' + id
  response = requests.get(URL)
  with open('storeCache.json', 'w') as storeData:
    json.dump(response.json()[0], storeData)
  
def getFromJSON(filename):
  with open(filename) as filedata:
    data = json.load(filedata)
  return data

if __name__ == "__main__":
  main()