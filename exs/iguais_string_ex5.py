string1 = str(input("insira uma palavra "))
string2 = str(input("insira outra palavra "))
for i in string1:
    string2 = string2.replace(i,"")
print(string2)