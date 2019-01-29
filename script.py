from winreg import *

Registry = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
RawKey = OpenKey(
    Registry, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Group Policy\Scripts\Startup\1\0")

key = QueryValueEx(RawKey, "Parameters")
text = key[0].split(" ")

username = text[0]
password = text[1]
print("""Användarnamnet är \"%s\" och lösenordet är \"%s\".""" %
      (username, password))
input()
