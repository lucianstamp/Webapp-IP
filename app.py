from flask import Flask, request, render_template, url_for, redirect, session, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

cred = credentials.Certificate("./pharmalinker1.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

pacienti_ref = db.collection('pacienti')
accounts_ref = db.collection('accounts')
comenzi_ref = db.collection('comenzi')
medicaccounts_ref = db.collection('medicaccounts')
robotlocation_ref = db.collection('robotlocation')


@app.route('/')
def start():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/index')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    pacienti = pacienti_ref.stream()
    pacienti_list = [{'id': pacient.id, **pacient.to_dict()} for pacient in pacienti]
    return render_template('index.html', pacienti=pacienti_list)


@app.route('/indexadmin')
def indexadmin():
    if 'user' not in session:
        return redirect(url_for('login'))
    pacienti = pacienti_ref.stream()
    pacienti_list = [{'id': pacient.id, **pacient.to_dict()} for pacient in pacienti]
    return render_template('indexadmin.html', pacienti=pacienti_list)


@app.route('/search', methods=['GET'])
def search():
    if 'user' not in session:
        return redirect(url_for('login'))
    nume = request.args.get('nume')
    if nume:
        query = pacienti_ref.where('nume', '==', nume).stream()
        pacienti_list = [{'id': pacient.id, **pacient.to_dict()} for pacient in query]
    else:
        pacienti_list = []
    return render_template('index.html', pacienti=pacienti_list)


@app.route('/searchadmin', methods=['GET'])
def searchadmin():
    if 'user' not in session:
        return redirect(url_for('login'))
    nume = request.args.get('nume')
    if nume:
        query = pacienti_ref.where('nume', '==', nume).stream()
        pacienti_list = [{'id': pacient.id, **pacient.to_dict()} for pacient in query]
    else:
        pacienti_list = []
    return render_template('indexadmin.html', pacienti=pacienti_list)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        nume = request.form.get('nume')
        varsta = int(request.form.get('varsta'))
        gen = request.form.get('gen')
        datanasterii = request.form['datanasterii']
        cnp = int(request.form.get('cnp'))
        adresa = request.form['adresa']
        telefon = int(request.form.get('telefon'))
        email = request.form.get('email')
        profesie = request.form.get('profesie')
        locdemunca = request.form.get('locdemunca')
        datainternare = request.form['datainternare']
        dataexternare = request.form['dataexternare']
        salon = int(request.form['salon'])
        pat = int(request.form['pat'])
        pacienti_ref.add({'nume': nume, 'varsta': varsta,'gen':gen, 'datanasterii': datanasterii, 'cnp': cnp, 'adresa': adresa, 'telefon': telefon, 'email': email, 'profesie': profesie, 'locdemunca': locdemunca, 'datainternare': datainternare, 'dataexternare': dataexternare, 'salon': salon, 'pat': pat})
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    pacient = pacienti_ref.document(id).get().to_dict()
    if request.method == 'POST':
        nume = request.form.get('nume')
        varsta = int(request.form.get('varsta'))
        gen = request.form.get('gen')
        datanasterii = request.form['datanasterii']
        cnp = int(request.form.get('cnp'))
        adresa = request.form['adresa']
        telefon = int(request.form.get('telefon'))
        email = request.form.get('email')
        profesie = request.form.get('profesie')
        locdemunca = request.form.get('locdemunca')
        datainternare = request.form['datainternare']
        dataexternare = request.form['dataexternare']
        salon = int(request.form['salon'])
        pat = int(request.form['pat'])
        pacienti_ref.document(id).update({'nume': nume, 'varsta': varsta,'gen': gen, 'datanasterii': datanasterii, 'cnp': cnp, 'adresa': adresa, 'telefon': telefon, 'email': email, 'profesie': profesie, 'locdemunca': locdemunca, 'datainternare': datainternare, 'dataexternare': dataexternare, 'salon': salon, 'pat': pat})
        return redirect(url_for('index'))
    return render_template('update.html', pacient=pacient)


@app.route('/updateadmin/<id>', methods=['GET', 'POST'])
def updateadmin(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    pacient = pacienti_ref.document(id).get().to_dict()
    if request.method == 'POST':
        nume = request.form.get('nume')
        varsta = int(request.form.get('varsta'))
        gen = request.form.get('gen')
        datanasterii = request.form['datanasterii']
        cnp = int(request.form.get('cnp'))
        adresa = request.form['adresa']
        telefon = int(request.form.get('telefon'))
        email = request.form.get('email')
        profesie = request.form.get('profesie')
        locdemunca = request.form.get('locdemunca')
        datainternare = request.form['datainternare']
        dataexternare = request.form['dataexternare']
        salon = int(request.form['salon'])
        pat = int(request.form['pat'])
        pacienti_ref.document(id).update({'nume': nume, 'varsta': varsta,'gen':gen, 'datanasterii': datanasterii, 'cnp': cnp, 'adresa': adresa, 'telefon': telefon, 'email': email, 'profesie': profesie, 'locdemunca': locdemunca, 'datainternare': datainternare, 'dataexternare': dataexternare, 'salon': salon, 'pat': pat})
        return redirect(url_for('indexadmin'))
    return render_template('updateadmin.html', pacient=pacient)

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    pacienti_ref.document(id).delete()
    return redirect(url_for('index'))

@app.route('/deleteadmin/<id>', methods=['POST'])
def deleteadmin(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    pacienti_ref.document(id).delete()
    return redirect(url_for('indexadmin'))

@app.route('/deletecomanda/<id>', methods=['POST'])
def deletecomanda(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    comanda = comenzi_ref.document(id).get().to_dict()
    pacient_id = comanda['pacient_id'] if comanda else None

    if pacient_id:
        comenzi_ref.document(id).delete()
        return redirect(url_for('comanda', id=pacient_id))
    else:
        return redirect(url_for('index'))

@app.route('/deletecomandaadmin/<id>', methods=['POST'])
def deletecomandaadmin(id):
    if 'user' not in session:
        return redirect(url_for('login'))

    comanda = comenzi_ref.document(id).get().to_dict()
    pacient_id = comanda['pacient_id'] if comanda else None

    if pacient_id:
        comenzi_ref.document(id).delete()
        return redirect(url_for('comandaadmin', id=pacient_id))
    else:
        return redirect(url_for('indexadmin'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        query = accounts_ref.where('email', '==', email).stream()
        user = [doc for doc in query]

        if user and user[0].to_dict().get('password') == password:
            session['user'] = user[0].id  # Store the user's document ID in session
            return redirect(url_for('indexadmin'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/loginmedicaccounts', methods=['GET', 'POST'])
def loginmedicaccounts():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        query = medicaccounts_ref.where('email', '==', email).stream()
        user = [doc for doc in query]

        if user and user[0].to_dict().get('password') == password:
            session['user'] = user[0].id
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        query = medicaccounts_ref.where('email', '==', email).stream()
        existing_user = [doc for doc in query]

        if existing_user:
            return render_template('register.html', error="Email already registered")

        user_ref = medicaccounts_ref.add({
            'email': email,
            'password': password
        })

        # Log in the user by storing their document ID in session
        session['user'] = user_ref[1].id
        return redirect(url_for('indexadmin'))
    return render_template('register.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/comanda/<id>', methods=['GET', 'POST'])
def comanda(id):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    if 'user' not in session:
        return redirect(url_for('login'))
    pacient = pacienti_ref.document(id).get().to_dict()
    if request.method == 'POST':
        medicament = request.form['medicament']
        diagnostic = request.form['diagnostic']
        comenzi_ref.add({'pacient_id': id, 'medicament': medicament,'diagnostic':diagnostic,'formatted_datetime':formatted_datetime , 'status': ""})
        return redirect(url_for('comanda', id=id))
    # History of orders
    comenzi = comenzi_ref.where('pacient_id', '==', id).stream()
    comenzi_list = [{'id': comanda.id, **comanda.to_dict()} for comanda in comenzi]

    return render_template('comanda.html', pacient=pacient, comenzi=comenzi_list)

@app.route('/comandaadmin/<id>', methods=['GET', 'POST'])
def comandaadmin(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    pacient = pacienti_ref.document(id).get().to_dict()
    comenzi = comenzi_ref.where('pacient_id', '==', id).stream()
    comenzi_list = [{'id': comanda.id, **comanda.to_dict()} for comanda in comenzi]

    return render_template('comandaadmin.html', pacient=pacient, comenzi=comenzi_list)


@app.route('/robotlocation')
def robotlocation():
    if 'user' not in session:
        return redirect(url_for('login'))
    robotlocation = robotlocation_ref.stream()
    robotlocation_list = [{'id': rblc.id, **rblc.to_dict()} for rblc in robotlocation]
    return render_template('map.html', robotlocation=robotlocation_list)


@app.route('/get_checkpoints')
def get_checkpoints():
    checkpoints_ref = db.collection('map')
    checkpoints = []
    for doc in checkpoints_ref.stream():
        checkpoint = doc.to_dict()
        checkpoint['id'] = doc.id
        checkpoints.append(checkpoint)
    return jsonify(checkpoints)

@app.route('/update_checkpoints', methods=['POST'])
def update_checkpoints():
    try:
        updates = request.json
        batch = db.batch()
        for checkpoint in updates:
            doc_ref = db.collection('map').document(checkpoint['id'])
            batch.set(doc_ref, {
                'front_id': checkpoint.get('front_id', "0"),
                'back_id': checkpoint.get('back_id', "0"),
                'left_id': checkpoint.get('left_id', "0"),
                'right_id': checkpoint.get('right_id', "0"),
                'x': checkpoint.get('x', 0),
                'y': checkpoint.get('y', 0),
            })
        batch.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Error updating checkpoints: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/delete_checkpoint/<id>', methods=['DELETE'])
def delete_checkpoint(id):
    try:
        db.collection('map').document(id).delete()
        return jsonify({"status": "success", "message": "Checkpoint deleted successfully"})
    except Exception as e:
        print(f"Error deleting checkpoint: {e}")
        return jsonify({"status": "error", "message": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
