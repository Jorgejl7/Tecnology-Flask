from flask import * #importamos tod de flask

app = Flask(__name__)

#Rutas de la pagina
@app.route('/')
def index():
	return render_template('index.html')