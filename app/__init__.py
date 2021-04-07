from flask import Flask

def create_app():
	app = Flask(__name__)

	@app.route('/')
	def index():
		return 'Hey there, this is index'

	@app.route('/new')
	def new_route():
		return 'Hey, your cicd worked successfully...😁'

	return app