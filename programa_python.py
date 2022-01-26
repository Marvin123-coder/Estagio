from asyncio.windows_events import NULL
import csv
from flask import Flask, render_template, request, abort, redirect, url_for

with open('ranking_novo.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    vetor = list(csv_reader)
    line_count = 0
    Anos = []
    Times = []
    for row in vetor:
        if line_count == 0:
            line_count += 1
        else:
            if row[1] not in Times:
                Times.append(row[1])
            if row[0] not in Anos:
                Anos.append(row[0])           
            line_count += 1

app = Flask(__name__,static_folder='templates')

resposta_time = []
resposta_ano = []
#resp = {"resposta": ""}

@app.route('/', methods=['GET', 'POST'])
def listas():
    if request.method == 'POST':
        try:
            if request.form['time'] in Times:
                resposta_time = []
                time_select = request.form['time']
                line_count = 0
                for row in vetor:
                    if line_count == 0:
                        line_count += 1
                    else:
                        if row[1] == time_select:
                            resposta_time.append(row)
                return redirect(url_for('resposta', lista=repr(resposta_time)))
        except: pass
        try:
            if request.form['ano'] in Anos:
                resposta_ano = []
                ano_select = request.form['ano']
                line_count = 0
                for row in vetor:
                    if line_count == 0:
                        line_count += 1
                    else:
                        if row[0] == ano_select:
                            resposta_ano.append(row)
                return redirect(url_for('resposta',lista=repr(resposta_ano)))
        except: pass
    else:
        pass
    return render_template('index.html',x=Times,y=Anos)

@app.route('/resposta', methods=['GET', 'POST'])
def resposta():
    return render_template('resposta.html',x=request.args.get("lista"))

if __name__ == '__main__':
    app.run(debug=True)