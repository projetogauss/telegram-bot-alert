import cx_Oracle
from utils import db_info


class ConnetionInterface():
    def createConnection():
        try:
            connection = cx_Oracle.connect(db_info.USER+'/'+db_info.PASS_WORD+'@'+db_info.IP+'/'+db_info.DB)   
        except cx_Oracle.DatabaseError as e:
            raise           
        return connection

