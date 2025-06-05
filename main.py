from flask import Flask, render_template, request, redirect, session, flash
import dati


app = Flask(__name__)

app.secret_key = 'random_bet_strong_secret_key'     # nepieciesams lai paraditu vai viss notiek veiksmigi

@app.route('/', methods=['POST','GET'])
def meklet():
    if 'lietotaj_vards' not in session:
        flash("Lai meklētu mājaslapas, lūdzu, pieslēdzieties.")
        return redirect('/login')

    if request.method == 'POST':
        if 'meklet' in request.form:
            Teksta_dala = request.form['teksts']
            teksta_ietvars = request.form['radiovariants']
            tagi = request.form.getlist('kategors[]')
            kverijs = dati.tekstapstrade(Teksta_dala, teksta_ietvars, tagi)
            rezultats = dati.nolasit(kverijs)
            kategorijas = dati.nolasit(1)
            elementi = dati.nolasit(2)
        elif 'dzest' in request.form:
            if session.get('loma') == 'admin':
                dati.dzest(request.form['dzestko'])
                flash("Saite dzēsta.")
            else:
                flash("Tikai admini drīkst dzēst saites.")
            rezultats = dati.nolasit()
            kategorijas = dati.nolasit(1)
            elementi = dati.nolasit(2)
    else:
        rezultats = []
        kategorijas = ["es"]
        elementi = []

    return render_template('index.html', linijas=rezultats, kategs=kategorijas, teksts=elementi)

@app.route('/login', methods=['POST','GET'])
def login_lapa():

        # nepieciesams lai paraditu vai viss notiek veiksmigi
       
    if request.method == 'POST':
        try:
            action = request.form.get("action")
            lietotaj_vards = request.form.get("username")
            parole = request.form.get("password")

            if action == 'login':
                rezultats, loma = dati.login_Lietotajs(lietotaj_vards, parole)
                flash(rezultats)
                if loma:
                    session['lietotaj_vards'] = lietotaj_vards
                    session['loma'] = loma
                    return redirect('/')
            elif action == 'register':
                rezultats = dati.izveidot_lietotaju(lietotaj_vards, parole)
                flash(rezultats)
        except Exception as e:
            return f"Kļūda: {str(e)}", 400  
    return render_template('login.html')
#beidzas nepieciesamais prieks parbaudes

@app.route('/logout')
def logout():
    session.clear()
    flash("Jūs esat atteicies.")
    return redirect('/')

@app.route('/pievienot', methods=['POST','GET'])
def pievienot_lapa():
    if session.get('loma') != 'admin':
        flash('Tikai admini var pievienot jaunas saites.')
        return redirect('/')
    
    if request.method == "POST":
        nosaukums = request.form.get('nosaukums')
        saite = request.form.get('saite')
        autors = request.form.get('Autors')
        anotacija = request.form.get('anotacija')
        saites = ['Nekas']
        
        print(f"Nosaukums: {nosaukums}, Saite: {saite}, Autors: {autors}, Anotācija: {anotacija}, {saites}")

        kverijaparametri1="'"+request.form['saite']+"'"','"'"+request.form['nosaukums']+"'"','"'"+request.form['anotacija']+"'"','"'"+request.form['Autors']+"'"
        jaunais_id=dati.ierakstit1(kverijaparametri1)
        saraksts = request.form.getlist('kategors[]')
        for elements in saraksts:
            dati.ierakstit2(elements,jaunais_id)

        elementi=dati.nolasit(2)
        kategorijas=dati.nolasit(1)
    else:
        saites = ["Nekas"]
        print(saites)
        elementi=[]
        kategorijas=["cits"]
    return render_template('pievienot.html',teksts=elementi, kategs=kategorijas, saraksts=saites)



if __name__ == '__main__' :
    app.run(port=5000)