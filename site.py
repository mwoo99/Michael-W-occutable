from flask import Flask, render_template
import occupations

app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome"

@app.route("/occupations")
def tablify():
	return render_template('occuhtml.html', jobDict = occupations.getDict(), randJob = occupations.randomPick())

if __name__ == "__main__":
	app.debug = True
	app.run()
	
