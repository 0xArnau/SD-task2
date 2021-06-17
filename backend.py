from lithops import Storage
import pandas as pd

class cosBackend:
    def __init__(self, config):
        self.config = config
        self.storage = Storage(config=config)

    def read_csv(self):
        return pd.read_csv('data.csv').to_string()

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
    def get_object(self, key):
        return self.storage.get_object(self.config['lithops']['storage_bucket'], key)

if __name__ == "__main__":
    from config.config import config

    #df = pandas.read_csv('data.csv').to_string()
    cos = cosBackend(config=config)
 
    # Get the last name & add 1
    next = (cos.list_keys(prefix='covid-19'))
    print(next)
 
    