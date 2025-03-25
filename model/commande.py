from model.connection import *
from model.repas import Repas
from datetime import datetime



class Commande(Base):
    def __init__(self, id_user = 0, date=''):
        self.id_user = id_user
        self.date = datetime.now()
        self.date_livraison = date
        self.total = 0
        self.status = 'attente de confirmation' """ Attente de confirmation;
                                                    Confirme;
                                                    Paye;
                                                    Livre;
                                                    """
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'Commande'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    id_user = Column('date', Integer)
    date_livraison = Column('date_livraison', String(255))
    total = Column('total', Integer)
    statut = Column('statut', String(255))


    def SearchCommande(self):
        session = self.Session()
        result = session.query(Commande).filter(Commande.id == self.id).first()
        session.commit()

        if result == None:
            return False
        return True
    
    def Update(self, id, id_user, date_livraison, total, statut):
        session = self.Session()
        result = session.query(Commande).filter(Commande.id == id).first()
        if result != None:
            if id_user != None:
                result.id_user = id_user
            if date_livraison != None:
                result.date_livraison = date_livraison
            if total!= None:
                result.total = total
            if statut != None:
                result.statut = statut
                        
            session.commit()
            return True
        return False
    
    def Delete(self, id):
        session = self.Session()
        result = session.query(Commande).filter(Commande.id == id).first()
        if result is not None:
            session.delete(result)
            session.commit()
            return True
        return False
    


    def Add_Commande(self):
        if self.SearchCommande():
            print('Ce Commande existe deja')
        else:
            try:
                session = self.Session()
                session.add(self)
                session.commit()
                session.refresh(self)
            except(sqlalchemy.exc.IntegrityError):
                print("Erreur Un tuple avec le meme id existe deja")
                
                
    def Get_total(self, id, id_user):
        session = self.Session()
        result = session.query(Commande_Repas).filter(Commande_Repas.id_commande == id).all()
        total = 0
        for i in result:
            repas = session.query(Repas).filter(Repas.id == i.id_repas).first()
            total += repas.prix * i.qnte
        return total
    
    def Get_Repas(self, id):
        session = self.Session()
        result = session.query(Commande_Repas).filter(Commande_Repas.id_commande == id).all()
        return result
                
                
                


class Commande_Repas(Base):
    def __init__(self, id_commande = 0, id_repas= 0, qnte = 1):
        self.id_commande = id_commande
        self.id_repas = id_repas
        self.qnte = qnte
        self.Session = sessionmaker(bind = engine)

    __tablename__ = 'Commande_Repas'
    id = Column('id', Integer, primary_key = True, autoincrement = True)
    id_commande = Column('id_commande', Integer)
    id_repas = Column('id_repas', Integer)
    qnte = Column('qnte', Integer)
    
    
    def Delete(self, id):
        session = self.Session()
        result = session.query(Commande_Repas).filter(Commande_Repas.id == id).first()
        if result is not None:
            session.delete(result)
            session.commit()
            return True
        return False
    


    def Add(self):
        if self.Search():
            print('Ce Commande existe deja')
        else:
            try:
                session = self.Session()
                session.add(self)
                session.commit()
                session.refresh(self)
            except(sqlalchemy.exc.IntegrityError):
                print("Erreur Un tuple avec le meme id existe deja")
    
    def Search(self):
        session = self.Session()
        result = session.query(Commande_Repas).filter(Commande_Repas.id == self.id).first()
        session.commit()

        if result == None:
            return False
        return True
    
    
    def Search_Return(self):
        session = self.Session()
        result = session.query(Commande_Repas).filter(Commande_Repas.id == self.id).first()
        session.commit()

        if result == None:
            return False
        return result
    
    
    
Base.metadata.create_all(engine)