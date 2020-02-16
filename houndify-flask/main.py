from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	print(request)
	print(request.get_json())
	username = request.args.get('inputName')
	useremail = request.args.get('inputEmail')
	# print(username)
	payload = (username, useremail)

	url = "https://demo.checkbook.io/v3/check/digital"
	# payload = json.dumps({'recipient': useremail, 'name': username, 'amount': 100, 'description': 'Drone Payment'})
	# headers = {
	#     'accept': "application/json",
	#     'content-type': "application/json",
	#     'authorization': "d6aa2703655f4ba2af2a56202961ca86:dXbCgzYBMibj8ZwuQMd2NXr6rtvjZ8"
	#     }
	payload = "{\"recipient\":\"" + useremail + "\",\"name\":\"" + username + "\",\"amount\":100,\"description\":\"Treehacks Demo!\"}"
	headers = {
	    'accept': "application/json",
	    'content-type': "application/json",
	    'authorization': "d6aa2703655f4ba2af2a56202961ca86:dXbCgzYBMibj8ZwuQMd2NXr6rtvjZ8"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)
	return(response.text)
	# return
	# if username is not None and useremail is not None:
	# 	print(payload)
	# return "Hi"

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)



# url = "https://demo.checkbook.io/v3/check/digital"

# payload = "{\"recipient\":\"akhand@stanford.edu\",\"name\":\"Widgets Inc.\",\"amount\":5,\"description\":\"Test Check\"}"
# headers = {
#     'accept': "application/json",
#     'content-type': "application/json"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)


