import time as t
from sendMsg import religacaoComDebito

def main():
    segundos = 240
    while 1:
        religacaoComDebito.sendAlert()
        for i in range(segundos):
            for a in range(segundos):
                print(str(segundos-a) + " segundos restantes para proxima busca. \n")
                t.sleep(1)
            #t.sleep(segundos)
            try:
                religacaoComDebito.sendAlert()
            except:
                """This aberration is because the telegram server return an error
                (ProtocolError 10045 conection refused by host remote)´ 
                and also because this app no can stop by nothing"""

                print('...Conection error with Telegram server')
                pass
            finally:
                t.sleep(60)
                #sendalert = religacaoComDebito()
                

            print('Busca executada!')

if __name__ == '__main__':
    main()

