from main import app

@app.route('/')
def index():
    return "Whaaat uuuuuuuup?"

@app.route('/fish/<id>')
def get_fish(id):
    print(id)
    return "my fish is beautiful"

@app.route('/fish', methods=['GET'])
def get_all_fishes():
    return "all fishes"

@app.route('/fish', methods=['POST'])
def create_fish():
    print("fish created")
    return "fish created"
