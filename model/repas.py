from model.connection import *



class Repas(Base):
    def __init__(self, name = '',photo = '', prix = '', type = ''):
        self.name = name
        self.photo = photo
        self.prix = prix
        self.type = type
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'Repas'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    name = Column('name', String(255))
    description = Column('description', String(1023))
    photo = Column('photo', String(255))
    prix = Column('prix', String(255))
    type = Column('type', String(255))


    def SearchRepas(self):
        session = self.Session()
        result = session.query(Repas).filter(Repas.name == self.name).first()
        session.commit()

        if result == None:
            return False
        return True
    
    def Get_repas(self):
        session = self.Session()
        result = session.query(Repas).filter(Repas.type== self.type).all()

        if result == None:
            return False
        return result
    
    def Get_repas_by_id(self, id):
        session = self.Session()
        result = session.query(Repas).filter(Repas.id== id).first()

        if result == None:
            return False
        return result
    
    def Get_all_type(self):
        session = self.Session()
        result = session.query(Repas.type).group_by(Repas.type).all()

        if result == None:
            return False
        return result[1:]
    
    def Get_id(self):
        session = self.Session()
        result = session.query(Repas).filter(Repas.name == self.name).first()
        return result.id
    
    def Update(self, id):
        session = self.Session()
        result = session.query(Repas).filter(Repas.id == id).first()
        if result != None:
            if self.name != '':
                result.name = self.name
            if self.description != '':
                result.description = self.description
            if self.prix != '':
                result.prix = self.prix
            if self.photo != '':
                result.photo = self.photo
            if self.type != '':
                result.type != self.type
            
            session.commit()
            return True
        return False
    
    def Delete(self, id):
        session = self.Session()
        result = session.query(Repas).filter(Repas.id == id).first()
        if result is not None:
            session.delete(result)
            session.commit()
            return True
        return False
    


    def Add_Repas(self):
        if self.SearchRepas():
            print('Ce repas existe deja')
        else:
            try:
                session = self.Session()
                session.add(self)
                session.commit()
                session.refresh(self)
            except(sqlalchemy.exc.IntegrityError):
                print("Erreur Un tuple avec le meme id existe deja")
                
                
class Composant(Base):
    def __init__(self, name = ''):
        self.name = name
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'Composant'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    name = Column('name', String(255))
    
    def Add(self):
        session = self.Session()
        session.add(self)
        session.commit()
        session.refresh(self)
        
    def Get_id(self):
        session = self.Session()
        result = session.query(Composant).filter(Composant.name == self.name).first()
        return result.id
    
    def Get_name(self):
        session = self.Session()
        result = session.query(Composant.name).filter(Composant.id == self.id).first()
        return result
    
    def Search(self):
        session = self.Session()
        result = session.query(Composant).filter(Composant.name == self.name).first()
        session.commit()

        if result == None:
            return False
        return True
    
    
        
class ComposantRepas(Base):
    def __init__(self, id_repas, id_composant):
        self.id_repas = id_repas
        self.id_composant = id_composant
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'ComposantRepas'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    id_repas = Column('id_repas', Integer)
    id_composant = Column('id_composant', Integer)
    
    
    def Add(self):
        session = self.Session()
        session.add(self)
        session.commit()
        session.refresh(self)
        
    def Search(self):
        session = self.Session()
        result = session.query(ComposantRepas).filter(ComposantRepas.id_repas == self.id_repas, ComposantRepas.id_composant == self.id_composant).first()
        session.commit()

        if result == None:
            return False
        return True
    
    def Search_composants_repas(self):
        session = self.Session()
        result = session.query(ComposantRepas.id_composant).filter(ComposantRepas.id_repas == self.id_repas).all()
        session.commit()

        if result == None:
            return False
        return result
        
    
        

Base.metadata.create_all(engine)