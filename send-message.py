#Author: Ayeed Shaikh
#Organisation: HexeSYS
#Email: hexesys@gmail.com


import urllib 
import urllib3 
from urllib.parse import urlencode

authkey = "YOUR API KEY" # Your authentication key.

mobiles = "8888888888" # Multiple mobiles numbers separated by comma.

message = "Welcome to msg91 send message feature." # Your message to send.

sender = "TESTIN" # Sender ID,While using route4 sender id should be 6 characters long.

route = "4" # Define route, used to send Transactional messages

http = urllib3.PoolManager()

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }




postdata = urlencode(values)

url = 'http://api.msg91.com/api/sendhttp.php?' + postdata
print(url)
r = http.request('GET', url)

print (r.data.decode('utf-8'))
print ("Contact Us at hexesys@gmail.com or visit our website www.hexesys.com incase any guidance for API integration)
