from flask import Flask, jsonify, request, Response
import requests
import re
import json

app = Flask(__name__)
proxies = list()
proxyNow = 0
api = "https://service.narvii.com/api/v1"

@app.route('/<path:path>', methods=["GET", "POST", "DELETE"])
def catch_all(path):
    global proxyNow
    if request.method == 'POST':
        result = requests.post(f"{api}/{path}", headers=request.headers, data=request.data, proxies=proxies[proxyNow])
        if proxyNow < len(proxies): proxyNow+=1
        else: proxyNow = 0
    elif request.method == 'GET':
        result = requests.get(f"{api}/{path}", headers=request.headers, proxies=proxies[proxyNow])
        if proxyNow < len(proxies): proxyNow+=1
        else: proxyNow = 0
    elif request.method == 'DELETE':
        result = requests.delete(f"{api}/{path}", headers=request.headers, proxies=proxies[proxyNow])
        if proxyNow < len(proxies): proxyNow+=1
        else: proxyNow = 0
    return Response(result.text, result.status_code, mimetype='application/json')
 
if __name__ == '__main__':
    with open("proxies.txt", "r") as file:
        for line in file:
            proxies.append({"https": line.replace('\\n', '')})
    print(f" * Loaded {len(proxies)} proxies!")
    
    app.run(host="0.0.0.0", port=55535, debug=True)
    