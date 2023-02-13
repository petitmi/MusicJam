from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

@app.route('/my', methods=['POST'])
def mytune():
    a = request.data
    print(a)
    return a

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # app = create_app()
    # gunicorn_logger = loggi ng.getLogger('gunicorn.error')
    # app.logger.handlers = gunicorn_logger.handlers
    # app.logger.setLevel(gunicorn_logger.level)
    app.run(host='0.0.0.0',port=8080,debug=True)
