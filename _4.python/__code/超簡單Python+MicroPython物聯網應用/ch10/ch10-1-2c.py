import uos

uos.mkdir("test")
print(uos.listdir())
uos.chdir("test")
print(uos.listdir())
uos.chdir("..")
print(uos.listdir())
