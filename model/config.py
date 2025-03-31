class Config:
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'bellarsene77@gmail.com'  # Remplacez par votre adresse Gmail
    MAIL_PASSWORD = 'nmio pihf rgae fvni' 
    
    MAIL_DEBUG = True
    MAIL_SUPPRESS_SEND = False
    
    MAIL_DEFAULT_SENDER = ('La cuisine de LETICIA', 'lacuisinedeleticia@gmail.com')
    MAIL_MAX_EMAILS = None
    
    MAIL_ASCII_ATTACHMENTS = False