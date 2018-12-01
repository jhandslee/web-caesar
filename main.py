from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True		# displays runtime errors in the browser

caesar_form = """
<!DOCTYPE html>
<html>
	<head>
		<style>
			form {
				bacground-color: #eee;
				padding: 20px;
				margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
			textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
		</style>
	</head>
	<body>
		<form action="/caesar" method="POST">
        <label for="caesar-cipher">Rotate by:</label>
        <input id="caesar-cipher" type="number" name="rot" value=0 />
        <textarea name="text">Enter text here</textarea>
        <input type="submit" />
        </form>
	</body>
</html>
		"""


@app.route("/caesar", methods=['POST'])
def encrypt():
	rot = request.form['rot']
	rot = int(rot)
	text = request.form['text']	
	return rotate_string(text, rot)

@app.route("/")
def index():
	return caesar_form

app.run()