from flask import Flask, jsonify, request
from list import final_list

app = Flask(__name__)

@app.route('/')
def show():
    return jsonify({
        'data': final_list,
        'status': 'success'
    }), 200

@app.route('/planet')
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in final_list if item['star_name'] == name)
    return jsonify({
        'data': planet_data,
        'status': 'success'
    }),200

if __name__ == '__main__':
    app.run()