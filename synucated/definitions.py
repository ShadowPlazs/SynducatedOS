def clear():
  print("\033c", end='')
  
def fetch(a):
  if a == "ip":
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
   
  else:
    raise Exception("unidentified input valuable 'a'")
