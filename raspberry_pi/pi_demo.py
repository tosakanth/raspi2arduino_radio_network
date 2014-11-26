from NRF24L01_wrapper import TK_RADIO
from time import gmtime,strftime

def parseData(data):
	humid=''
	temp=''
	station=''
	for i in range(5):
		humid=humid+chr(data[i])
	for i in range(5,10):
		temp=temp+chr(data[i])
	for i in range(10,15) :
		station=station+chr(data[i])
	print "Humidity : %s percent" % (humid)
	print "Temperature : %s" % (temp)
	print "From station : %s" % (station)
	print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
	print "=============================="			

tk_radio = TK_RADIO()
tk_radio.begin()
readingPipes=[[0xF0, 0xF0, 0xF0, 0xF0, 0xC2],[0xF0, 0xF0, 0xF0, 0xF0, 0xC3],[0xF0, 0xF0, 0xF0, 0xF0, 0xC4],[0xF0, 0xF0, 0xF0, 0xF0, 0xC5]]
tk_radio.openReadingPipes(readingPipes)
tk_radio.showDetails()

stop_flag=False

try:
	while True:
		recv_buf= []		
		recv_buf=tk_radio.get_msg()		
		if recv_buf != [] :
			parseData(recv_buf)
		#out = ''.join(chr(i) for i in recv_buf)
		#if out != '':
		#	print out
   
except KeyboardInterrupt:
   tk_radio.close();


