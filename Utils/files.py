import pickle
from user import user1 


entrada= open("binary.txt","wb")
pickle.dump(user1,entrada)
entrada.close()

salida=open("binary.txt","rb")
datos=pickle.load(salida)
print(datos)
salida.close()



















