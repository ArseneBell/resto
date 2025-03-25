from model.connection import *



class User(Base):
    def __init__(self, username = '', email = '', tel = '', password = ''):
        self.username = username
        self.email= email
        self.tel = tel
        self.password = password
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'User'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    username = Column('username', String(255))
    tel = Column('tel', String(255))
    email = Column('email', String(255))
    password = Column('mot_de_pass', String(255), nullable = True)


    def SearchUser(self):
        session = self.Session()
        result = session.query(User).filter(User.username == self.username and User.password == self.password).first()
        session.commit()

        if result == None:
            return False
        return True
    
    def Get_id(self):
        session = self.Session()
        result = session.query(User).filter(User.username == self.username).first()
        return result.id
    
    def Update(self, id):
        session = self.Session()
        result = session.query(User).filter(User.id == id).first()
        if result != None:
            if self.username != '':
                result.username = self.username
            if self.email != '':
                result.email = self.email
            if self.password != '':
                result.password = self.password
            if self.tel != '':
                result.tel = self.tel
            session.commit()
            return True
        return False
        

    

    def Connexion(self):
        session = self.Session()
        result = session.query(User).filter(User.username == self.username and User.password == self.password).first()
        if result == None:
            return False
        return True

    def Add_user(self):
        if self.SearchUser():
            print('Un utilisateur similaire existe deja')
        else:
            try:
                session = self.Session()
                session.add(self)
                session.commit()
                session.refresh(self)
            except(sqlalchemy.exc.IntegrityError):
                print("Erreur Un tuple avec le meme id existe deja")
                

Base.metadata.create_all(engine)