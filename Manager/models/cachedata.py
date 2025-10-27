from ..myredis import MyRedis as Redis
import os
import sys

GAME_SERVER="game"

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
           self._redis = Redis();
           if self._redis.ping():
              self.details["Redis"]["Status"] = True
       except Redis.ConnectionError:
              self.details["Redis"]["Status"] = False
              return     
       # Check Application status
       if self._redis.getKey("SYSTEM:SIMULATOR PROCESS") == "RUNNING" :
           self.details["Application"]["Status"] = True
       else:
           self.details["Application"]["Status"] = False
           return  # Not much point in going further if the app is not running
       
       # Check Simulator status
       if self._redis.getKey("SYSTEM:PAUSED") == "True" :
           self.details["Simulator"]["Status"] = False
       else:
           self.details["Simulator"]["Status"] = True

    def ping_server(self, host):
        command = "ping -n 1 " if sys.platform.lower()=="win32" else "ping -c 1 "
        response = os.system(f"{command} {host}") 
        return response == 0


