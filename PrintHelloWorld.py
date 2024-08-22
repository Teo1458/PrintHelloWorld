import time
import string

print('Inserisci il testo:')
testo=input()

alfabeto = string.ascii_letters+string.punctuation+' '
appoggio=''

h=0
while len(testo) != h:
    for i in range (len(alfabeto)):

        if alfabeto[i] != testo[h]:
            
            print (appoggio + alfabeto[i], end ='\r')
            time.sleep(0.05)
        elif alfabeto[i] == testo[h]:
                appoggio = (appoggio + testo[h])
                h+=1
                
                print (appoggio)
                time.sleep (0.05)