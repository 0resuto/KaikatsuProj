from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        return "Нет соединения."
    elif request.method == "POST":
        payload = request.json
        user_response = (payload['queryResult']['queryText'])
        bot_response = (payload['queryResult']['fulfillmentText'])
        if user_response or bot_response != "":
            print("Orest: " + user_response)
            print("Kaikatsu: " + bot_response)
        return "message received."
    else:
        print (request.data)
        return "200"
 
 
 
if __name__ == '__main__':
    app.run(debug=True)

