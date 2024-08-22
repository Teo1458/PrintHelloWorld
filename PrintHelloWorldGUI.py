import time
import string
from appJar import gui
win = gui('Hello World!')
win.setSize('300x300')

def press(name):
    if name == 'Invio':
        testo = win.getEntry('Inserisci il testo')
        
        alfabeto = string.ascii_letters+string.punctuation+' '
        appoggio=''

        h=0
        while len(testo) != h:
            for i in range (len(alfabeto)):

                if alfabeto[i] != testo[h]:
                    #update label testo Textbox
                    print (appoggio + alfabeto[i], end ='\r')
                    time.sleep(0.05)
                elif alfabeto[i] == testo[h]:
                        appoggio = (appoggio + testo[h])
                        h+=1
                        #update label testo Textbox
                        print (appoggio)
                        time.sleep (0.05)



win.addLabelEntry('Inserisci il testo')
win.addButton('Invio',press)
win.setFocus('Inserisci il testo')






win.go()