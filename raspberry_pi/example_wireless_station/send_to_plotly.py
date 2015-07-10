from NRF24L01_wrapper import TK_RADIO
from time import gmtime,strftime
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects

#plotly setup

username = 'your usename'
api_key = 'your api key'
stream_token = ['your tokens']

py.sign_in(username,api_key )

trace1 = Scatter(
    x=[],
    y=[],
    name="soil_moisture",
    stream=dict(
        token=stream_token[0],
        maxpoints=200
    )
)
trace2 = Scatter(
    x=[],
    y=[],
    name="temperature",
    stream=dict(
        token=stream_token[1],
        maxpoints=200
    )
)
trace3 = Scatter(
    x=[],
    y=[],
    name="humidity",
    stream=dict(
        token=stream_token[2],
        maxpoints=200
    )
)
layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)
fig = Figure(data=[trace1,trace2,trace3], layout=layout)
py.plot(fig, filename='Raspberry Pi Streaming Example Values')

stream0 = py.Stream(stream_token[0])
stream1 = py.Stream(stream_token[1])
stream2 = py.Stream(stream_token[2])

stream0.open()
stream1.open()
stream2.open()

def parseData(data):
	humid=''
	temp=''
	station=''
	soil_moist=''
	
	for i in range(5) :
		station=station+chr(data[i])
	if station=='00001' :
		for i in range(5,9) :
			soil_moist=soil_moist+chr(data[i]) 
		
		#print "Soil Moisture : %s " % (soil_moist)
		stream0.write({'x': strftime("%M:%S", gmtime()), 'y': 100-int(soil_moist)*100/1023})
	elif station=='00002' :	
		for i in range(5,10):
			humid=humid+chr(data[i])
		for i in range(10,14):
			temp=temp+chr(data[i])
		stream1.write({'x': strftime("%M:%S", gmtime()), 'y': temp})
		stream2.write({'x': strftime("%M:%S", gmtime()), 'y': humid})	

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
   
except KeyboardInterrupt:
   tk_radio.close();

