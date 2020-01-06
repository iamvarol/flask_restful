from flask import Flask, jsonify, request 

app = Flask(__name__)

toys = [{'name' : 'Play Mat'}, 
        {'name' : 'Activity Blocks'}, 
        {'name' : 'Giraffe Teether'}, 
        {'name' : 'Bounce and Spin Puppy'},
        {'name' : 'Activity Center'},
        {'name' : 'Piano and Gym'},
        ]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'Welcome Toddlers Toys!'})

@app.route('/toy', methods=['GET'])
def returnAll():
	return jsonify({'toys' : toys})

@app.route('/toy/<string:name>', methods=['GET'])
def returnOne(name):
	t = [toy for toy in toys if toy['name'] == name]
	return jsonify({'toy' : t[0]})


@app.route('/toy', methods=['POST'])
def addOne():
    # toy = {'name' : request.json(['name'])}
    toy = request.get_json('name')
    toys.append(toy)
    return jsonify({'toys' : toys})

@app.route('/toy/<string:name>', methods=['PUT'])
def editOne(name):
	t = [toy for toy in toys if toy['name'] == name]
	t[0]['name'] = request.json['name']
	return jsonify({'toy' : t[0]})


@app.route('/toy/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [toy for toy in toys if toy['name'] == name]
	toys.remove(lang[0])
	return jsonify({'toys' : toys})

if __name__ == '__main__':
	app.run(debug=True, port=1068) #run app on port 1068 in debug mode
