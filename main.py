import lithops

#fexec = lithops.FunctionExecutor(runtime='arppi/sd-lithops-custom-runtime:0.1')
fexec = lithops.ServerlessExecutor()
def hello(data):
  return f"Hello {data}"

future = fexec.call_async(hello, 'world')
