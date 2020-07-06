import time as t
from sendMsg import religacaoComDebito

def main():
    segundos = 10
    while 1:
        religacaoComDebito.sendAlert()
        for i in range(segundos):
            for a in range(segundos):
                print(str(segundos-a) + " segundos restantes para proxima busca. \n")
                t.sleep(1)
            #t.sleep(segundos)
            religacaoComDebito.sendAlert()
            print('Busca executada!')

if __name__ == '__main__':
    main()

