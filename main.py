import os, requests, traceback
os.system('pip install -r requirement.txt')
i = requests.get(os.environ['main'])
try:
  exec(i.content)
except:
  tracebacks = traceback.format_exc().replace("""  File "main.py", line 4, in <module>
   exec(i.content)
  """, '')
  print(tracebacks)
