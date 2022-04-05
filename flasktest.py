from flask import Flask
from PyP100 import PyP100

p100 = PyP100.P100("192.168.219.101", "kty222222@naver.com", "taewan12") #Creating a P100 plug object
p100.handshake() #Creates the cookies required for further methods
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods

app = Flask(__name__)



@app.route('/')
def hello_world():
	return 'Min hee welcome'

@app.route('/turnon')
def turnon():
    p100.turnOn()
    return 'complete'

@app.route('/turnoff')
def turnoff():
    p100.turnOff()
    return 'complete'

if __name__ == '__main__':

	app.run(host="192.168.219.102", port="80")

