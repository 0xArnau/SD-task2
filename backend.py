from lithops import Storage
#from config.config import config
import pandas

class cosBackend:
    def __init__(self, config):
        self.config = config
        self.storage = Storage(config=config)

    def read_csv(self):
        return pandas.read_csv('data.csv').to_string()

    def list_keys(self, prefix):
        return self.storage.list_keys(self.config['lithops']['storage_bucket'], prefix=prefix+'/')

    def put_object(self, prefix, name, ext, body):
        next = self.list_keys(prefix=prefix)
        
        if next == []:
            next = '{}/{}0001.{}'.format(prefix, name, ext)
        else:
            next = next[-1][-8:-4]
            next = (f"{prefix}/{name}{int(next) + 1:04d}.{ext}")
            
        self.storage.put_object(
            bucket='urv.sd.task2',
            key=next,
            body=body
        )

if __name__ == "__main__":
   klk = cosBackend(config=config)
   klk.put_object('', 'data', 'txt')
"""
    df = pandas.read_csv('data.csv').to_string()
    storage = Storage(config=config)


   
    # Get the last name & add 1
    next = (storage.list_keys(config['lithops']['storage_bucket']))
    if next == []:
        next = 'data0001.csv'
    else:
        next = next[-1][-8:-4]
        print(next)
        next = (f"data{int(next) + 1:04d}.csv")
        
    storage.put_object(bucket='urv.sd.task2',
                       key=next,
                       body=df)
"""  
    