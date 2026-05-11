import uos

uos.rmdir("test")
print(uos.listdir())
uos.remove("data.txt")
print(uos.listdir())