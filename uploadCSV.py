from lithops import Storage
from config.config import config
import pandas

if __name__ == "__main__":

    df = pandas.read_csv('data.csv').to_string()
    storage = Storage(config=config)


   
    # Get the last name & add 1
    next = (storage.list_keys(config['lithops']['storage_bucket'])[-1][4:8])
    next = (f"data{int(next) + 1:04d}.csv")
    
    storage.put_object(bucket='urv.sd.task2',
                       key=next,
                       body=df)
    
    