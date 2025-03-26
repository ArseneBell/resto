from flask import Flask, render_template,request, redirect, url_for, session as sess, flash, jsonify
import secrets
from model.repas import *
from model.user import *
from model.commande import *

app = Flask('__name__')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.secret_key = secrets.token_hex(16)


@app.route('/')
def index():
    r = Repas(type='fast Food')
    repas = r.Get_repas()
    print(repas)
    return render_template('index.html')


@app.route('/menu')
def menu(tpe = 'Fast Food'):
    
    all_type = Repas().Get_all_type()
    all_types = []
    for type in all_type:
        all_types.append(type[0])
    
    tpe = 'Fast Food'
    r = Repas(type=tpe)
    try:
        tpe = request.args.get('type')
        r = Repas(type=tpe)
    except:
        pass 
    
    repas = r.Get_repas()                      
          
    return render_template('menu.html', repas=repas, type=tpe, all_types=all_types)


@app.route('/modif/<id>')
def modif(id):
    repas = Repas().Get_repas_by_id(id)
    
    
    return render_template('modif.html', repas=repas)

@app.route('/update_repas', methods=['POST'])
def update_repas():
    data = request.json  # Récupère les données JSON envoyées par le client

    # Exemple de traitement des données
    repas_name = data.get('name')
    repas_type = data.get('type')
    repas_prix = data.get('prix')
    repas_id   = data.get('id')

    # Vous pouvez ajouter ici la logique pour mettre à jour la base de données
    repas = Repas(name=repas_name, type=repas_type, prix=repas_prix).Update(repas_id)
    print(repas)
    

    return jsonify({'message': 'Données reçues avec succès', 'status': 'success'})

if __name__ == '__main__':
    app.run(app, host='0.0.0.0', port=5000, debug=True)