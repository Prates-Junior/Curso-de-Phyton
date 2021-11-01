arquivo = open("README.txt","r")
print(arquivo.readlines())
arquivo.seek(0)
print(arquivo.read().split("\n"))
arquivo.seek(0)

for linha in arquivo.readlines():
    if "https://" in linha:
        print(linha)

        
        arquivo = open("README.txt","r")
url = []
for linha in arquivo.readlines():
    if "https//" in linha:
        url = linha[linha.find("https://"):]
    url.append(url)
    print(url)

arquivo.close()

