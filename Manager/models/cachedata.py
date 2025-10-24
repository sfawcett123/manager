from ..myredis import MyRedis as Redis
import os

GAME_SERVER="game.local"

class CacheData:
    details={ "Redis":       {"Name": "Redis"      , "Status": False  },   
              "Server":      {"Name": "Server"     , "Status": False  },
              "Application": {"Name": "Application", "Status": False  },
              "Simulator":   {"Name": "Simulator"  , "Status": False  }}

    def __init__(self, refresh=True):

       if refresh:
            self.RefreshData()
           
    def RefreshData( self ):
       # Check server status
       self.details["Server"]["Status"] = self.ping_server(GAME_SERVER)
       
       # Check Redis status
       try:
           self.connection = Redis()
           if self.connection.ping():
              self.details["Redis"]["Status"] = True
       except Redis.ConnectionError:
              self.details["Redis"]["Status"] = False
              return     
       # Check Application status
       if self.getRedisKey("SYSTEM:SIMULATOR PROCESS") == "RUNNING" :
           self.details["Application"]["Status"] = True
       else:
           self.details["Application"]["Status"] = False
           return  # Not much point in going further if the app is not running
       
       # Check Simulator status
       if self.getRedisKey("SYSTEM:PAUSED") == "True" :
           self.details["Simulator"]["Status"] = False
       else:
           self.details["Simulator"]["Status"] = True

    def ping_server(self, host):
        response = os.system(f"ping -n 1 {host}") 
        return response == 0

    def getRedisKey( self , key ):
        value = self.connection.get(key)
        print(f"Key: {key} Value: {value}")
        return value.decode('utf-8') if value else None

