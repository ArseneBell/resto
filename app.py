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


if __name__ == '__main__':
    app.run(app, host='0.0.0.0', port=5000, debug=True)