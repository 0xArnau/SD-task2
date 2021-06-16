import lithops
from config.config import config


#fexec = lithops.FunctionExecutor(config=config,runtime='arppi/sd-lithops-custom-runtime-38:0.1')
def my_function(x):
    return x + 7


if __name__ == '__main__':
    fexec = lithops.FunctionExecutor(config=config)
    fexec.call_async(my_function, 3)
    print(fexec.get_result())
