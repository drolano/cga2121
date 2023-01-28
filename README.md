## Technicolor CGA2121 Gateway Scraper library

This is a library to use in order to scrape Technicolor Gateway CGA2121

### Installation


`pip install cga2121`


### How to use it



```
from cga2121 import Cga2121
    
gateway = Cga2121("192.168.0.1", "80", "user", "pass")
  
gateway.authenticate()
  
devices = gateway.get_device_modal()
  
```
 
