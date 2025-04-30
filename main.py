from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index_lapa():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login_lapa():
    return render_template('login.html')

@app.route('/pievienot', methods=['POST','GET'])
def pievienot_lapa():
    kategorijas = ['Smieklīgi', 'Izglītojoši', 'Motivējoši']  
    
    if request.method == "POST":
        saite = request.form.get('saite')
        anotacija = request.form.get('anotacija')
        autors = request.form.get('Autors')

        
        print(f"Saite: {saite}, Anotācija: {anotacija}, Autors: {autors}")

    return render_template('pievienot.html', kategorijas=kategorijas)




if __name__ == '__main__' :
    app.run(port=5000)