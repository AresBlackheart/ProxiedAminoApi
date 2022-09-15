from flask import Flask, jsonify, request, Response
import requests
import re
import json

app = Flask(__name__)
proxyList = list()
proxyNow = 0
api = "https://service.narvii.com/api/v1"

@app.route('/')
def index():
    return '''<html> <head> <title>403 Forbidden</title> </head>
			<body> <center><h1>403 Forbidden</h1></center> </body>
			</html>'''

@app.route('/<path:path>', methods=["GET", "POST", "DELETE"])
def catch_all(path):
    global proxyNow
    if request.method == 'POST':
        result = requests.post(f"{api}/{path}", headers=request.headers, data=request.data, proxies=proxyList[proxyNow])
        if proxyNow < len(proxyList): proxyNow+=1
        else: proxyNow = 0
    elif request.method == 'GET':
        result = requests.get(f"{api}/{path}", headers=request.headers, proxies=proxyList[proxyNow])
        if proxyNow < len(proxyList): proxyNow+=1
        else: proxyNow = 0
    elif request.method == 'DELETE':
        result = requests.delete(f"{api}/{path}", headers=request.headers, proxies=proxyList[proxyNow])
        if proxyNow < len(proxyList): proxyNow+=1
        else: proxyNow = 0
    return Response(result.text, result.status_code, mimetype='application/json')
 
if __name__ == '__main__':
    with open("proxies.txt", "r") as file:
        for line in file:
            proxyList.append({"https": line.strip()})
    print(f" * Loaded {len(proxyList)} proxies!")
    print(proxyList[0])
    
    app.run(host='0.0.0.0', port=55535, debug=True)
