from flask import Flask, jsonify,request, render_template, redirect
import requests, random
app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods = ['POST'])
def get_facts():
    name= request.json.get('name')
    email= request.json.get('email')
    year= request.json.get('year')
    color= request.json.get('color')
    num = random.randint(1,100)
    num_response = requests.get(f'http://numbersapi.com/{num}?min=1&max=100').content.decode('utf-8')
    year_response = requests.get(f'http://numbersapi.com/{year}/year').content.decode('utf-8')
    print('****************************')
    print(year_response, num_response)
    print('*****************************')
    return jsonify({'name':name, 'year': year, 'year_fact': year_response, 'num': num,'num_fact':num_response})