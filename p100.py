from PyP100 import PyP100

p100 = PyP100.P100("192.168.219.101", "kty222222@naver.com", "taewan12") #Creating a P100 plug object

p100.handshake() #Creates the cookies required for further methods
p100.login() #Sends credentials to the plug and creates AES Key and IV for further methods

#p100.turnOn() #Sends the turn on request
p100.turnOff()