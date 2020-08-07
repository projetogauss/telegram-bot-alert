
#import telepot
import telepot
import datetime
import time
from utils import key
from utils import querys
from socket import error as SocketError
import errno

#"from" inform any package or folder
#"import" inform any function or class

#import of the class reponsible by creation at conection as the database
from conn import ConnetionInterface
#instance of connection
class religacaoComDebito():
    def sendAlert():
        con = ConnetionInterface.createConnection()


#1-select of table with all ri with debit, and create a new table "temp" with all ri of the last
#query
#2 - left join in table ri_debit and send ri wich no are in temp 
#3 - cronc or schedule taks for execute the script of times in times

#cursor for query execution
        cursor = con.cursor()
#query here
        cursor.execute(querys.QUERY_RELIGAS)
#this detail is very important the cursor retorn a obj cursor.fetchall return 
# the register of query 
        rows = cursor.fetchall()


#telepot.Bot validate of id e key of Bot
        #bot = telepot.Bot(key.TOKEN_PROD)
        bot = telepot.Bot(key.TOKEN_TEST)
#here is the interation of the quety registers and buid of messager for send by
#Bot 
        i = 0
        tmp = 5 #time of interval between each send msg
        for row in rows:
            tempo = datetime.datetime.now()
            i += 1
            print (tempo)
            print ('Enviado ' + str(i))
            print ('Esperando '+str(tmp)+' segundos ....')
            time.sleep(tmp)  
 
            bot.sendMessage(key.CHAT_ID_TEST,'RELIGAÇÃO ABERTA COM DÉBITO' +'\n'+
                          'Regional: ' + str(row[13])+'\n'+
                          'Base: ' + str(row[14])+'\n'+
                          'Localidade: ' + str(row[15])+'\n'+
                          'Bairro: ' + str(row[11])+'\n'+
                          'Município: ' + str(row[16])+'\n'+                          
                          'Conta Contrato: ' + str(row[1])+'\n'+
                          'Tipo de Classe: ' + str(row[17])+'\n'+
                          'Cliente: ' + str(row[18])+'\n'+
                          'Instalação: ' + str(row[12])+'\n'+
                          'Nota: ' + str(row[0])+'\n'+
                          'Data: ' + str(row[7])+'\n'+
                          'Horário: ' + str(row[8])+'\n'+                          
                          'Valor em AB: ' + str(row[6])+'\n'+
                          'Telemedido: ' + str(row[10]) +'\n'+                      
                          'Usuário: ' + str(row[3]) +'\n'+
                          'Nome: ' + str(row[4])+'\n'+
                          'Gerencia: ' + str(row[5])
                          )
 

            oracle_insert_query = querys.QUERY_SAVE_RELIGAS
            register_insert = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            cursor.execute(oracle_insert_query, register_insert)
            con.commit()
            #close connection
        if con:
                cursor.close()
                print ('Cursor Fechado!!!')
                con.close()
                print('Conexao Fechada!!!')
                 


    