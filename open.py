arquivo = open("README.txt","r")
print(arquivo.readlines())
arquivo.seek(0)
print(arquivo.read().split("\n"))
arquivo.seek(0)

for linha in arquivo.readlines():
    if "https://" in linha:
        print(linha)


