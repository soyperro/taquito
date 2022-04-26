from flask import Flask, render_template, redirect, request, url_for, flash
from paradigma.core.summer import paracore
# from paradise_core.core_nn.summer import paradise
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

'''@app.route('/paradise', methods=['GET','POST'])
def paradise_nighcore():
    if request.method=='POST':
        text = request.form['texto']
        #number = request.form['lineas']
        #number = int(number)
        if len(text):
            get_stream = paradise()
            result = get_stream.paradise_core(text)
            flash('Se creó correctamente el resumen')
            return render_template('result.html', obtener_resultado=result) 
        else:
            flash('Error al crear el resumen, faltó introducir texto')
            return render_template('result_err.html')   
    return render_template('load_text4paradise.html')
'''

@app.route('/resumen', methods=['GET','POST'])
def result():
    if request.method=='POST':
        text = request.form['texto']
        number = request.form['lineas']
        #number = int(number)
        if len(number) and len(text):
            get_stream = paracore()
            result = get_stream.makemesmile(text, number)
            flash('Se creó correctamente el resumen')
            return render_template('result.html', obtener_resultado=result) 
        else:
            flash('Error al crear el resumen, faltó introducir texto o número de líneas')
            return render_template('result_err.html')   
    return render_template('load_text.html')

'''@app.route('/paradox')
def get_paradise():
    return render_template('load_text4paradise.html')
'''
@app.route('/')
def get_texto():
    return render_template('load_text.html')

if __name__=='__main__':
    app.run(debug=True)