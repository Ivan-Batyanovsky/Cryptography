from pygost import gost34112012256

print(gost34112012256.new("Батяновский Иван Тарасович".encode('utf-8')).digest().hex()[-1])
