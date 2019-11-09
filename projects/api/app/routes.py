from app import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
  return 'hello world'
