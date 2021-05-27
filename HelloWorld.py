from lithops import Storage
from config.config import config

if __name__ == "__main__":
    storage = Storage(config=config)
    storage.put_object(bucket='urv.sd.task2',
                       key='test.txt',
                       body='Hello World')
    
    print(storage.get_object(bucket='urv.sd.task2',
                             key='test.txt'))