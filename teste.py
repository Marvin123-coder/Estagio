from flask import Flask, request

app = Flask(__name__,static_folder='programa')

@app.route('/add', methods=["GET",POST"])
def add():
    return "OKK"

if __name__ == '__main__':
    app.run(debug=True)