import mysql.connector
import ConfigParser

class Mysql_Connector(object):
    
    def mysql_connect(self, environment='production'):
        self.config = ConfigParser.RawConfigParser()
        self.config.read('config/mysql.config')

        self.credentials = {'host' : self.get_field(environment, 'host'),
                            'user' : self.get_field(environment, 'user'),
                            'password' : self.get_field(environment, 'password'),
                            'database' : self.get_field(environment, 'database')}

        self.cnx = mysql.connector.connect(**self.credentials)
        

    def get_field(self, environment, field):
        return self.config.get(environment + "_mysql_connection", field)
        

    def mysql_query(self, query, fetch=False):
        cursor = self.cnx.cursor()
        cursor.execute(query)

        if fetch:
            cursor.fetchall()
            return cursor

        return cursor


        
