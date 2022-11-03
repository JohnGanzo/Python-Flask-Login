class Config:
    SECRET_KEY = 'AJGR'

class DevelopmentCofig(Config):
    #se crea la clase para poder iniciar el servidor en modo depuracion
    DEBUG=True
    # Configuracion para la base de datos
    MYSQL_HOST = '-----'
    MYSQL_USER = '-----'
    MYSQL_PASSWORD = '-----'
    MYSQL_DB = '-------'

#Se crea un diccionario que contiene la clase  
config={
    'development':DevelopmentCofig
}