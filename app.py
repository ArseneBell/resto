from flask import Flask, render_template,request, redirect, url_for, session, flash, jsonify
import secrets
from model.repas import *
from model.user import *
from model.commande import *
import os
from datetime import timedelta


app = Flask('__name__')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.secret_key = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)


UPLOAD_FOLDER = 'static/img/repas'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    if 'nb' not in session:
        session['nb'] = 0
        session['panier'] = []
    r = Repas(type='fast Food')
    repas = r.Get_repas()
    print(repas)
    return render_template('index.html')


@app.route('/menu')
def menu(tpe = 'Fast Food'):
    
    all_type = Repas().Get_all_type()
    all_types = ['all']
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
    if tpe == 'all':
        repas =  r.Get_repas_all()                    
          
    return render_template('menu.html', repas=repas, type=tpe, all_types=all_types)


@app.route('/modif/<id>')
def modif(id):
    repas = Repas().Get_repas_by_id(id)
    composants_repas = ComposantRepas(id).Search_composants_repas()
    composants = []
    for comp in composants_repas:
        composants.append(Composant().Get_name(int(comp[0])))
    
    
    return render_template('modif.html', repas=repas, composants=composants)

@app.route('/update_repas', methods=['POST'])
def update_repas():
    data = request.json  # Récupère les données JSON envoyées par le client
    print(data)  # Affiche les données reçues dans la console

    # Exemple de traitement des données
    repas_name = data.get('name')
    repas_type = data.get('type')
    repas_prix = data.get('prix')
    repas_id   = data.get('id')
    composants = data.get('composants')

    # Vous pouvez ajouter ici la logique pour mettre à jour la base de données
    repas = Repas(name=repas_name, type=repas_type, prix=repas_prix).Update(repas_id)
    print(repas)
    

    return jsonify({'message': 'Données reçues avec succès', 'status': 'success'})



@app.route('/upload_photo', methods=['POST'])
def upload_photo():
    if 'photo' not in request.files:
        return jsonify({'message': 'Aucun fichier reçu', 'status': 'error'}), 400

    file = request.files['photo']
    repas_id = request.form.get('id') # Récupère l'ID du repas

    if file.filename == '':
        return jsonify({'message': 'Aucun fichier sélectionné', 'status': 'error'}), 400

    # Enregistrer le fichier
    file.filename = Repas().Get_repas_by_id(repas_id).photo
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({'message': 'Fichier envoyé avec succès', 'status': 'success', 'file_path': file_path})


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json  # Récupère les données JSON envoyées par le client
    repas_id = data.get('id')  # Récupère l'ID du repas
    
    repas = Repas().Get_repas_by_id(repas_id)
    session['nb'] += 1  # Incrémenter le nombre de repas dans le panier

    # Exemple de traitement : Ajouter l'ID à une liste de panier (ou base de données)
    print(f"Repas ajouté au panier : {repas_id}")

    return jsonify({'message': 'Repas ajouté au panier avec succès', 'nb':session['nb'], 'status': 'success'})

if __name__ == '__main__':
    app.run(app, host='0.0.0.0', port=5000, debug=True)