from nrf24 import NRF24
import time

class P2PNetwork:
	
	def __init__(self,spi_major=0,spi_minor=0,ce_pin=25,irq_pin=18,write_pipe = [0xF0, 0xF0, 0xF0, 0xF0, 0xA1],read_pipe= [0xF0, 0xF0, 0xF0, 0xF0, 0xA2]):
		
		self.spi_major=spi_major
		self.spi_minor=spi_minor
		self.ce_pin=ce_pin
		self.irq_pin=irq_pin
		self.retrie_delay=15 #15*250usec
		self.retrie_times=15 #retry 15 times
		self.payload_size=20
		self.channel=90
		self.data_rate=NRF24.BR_1MBPS
		self.palevel=NRF24.PA_MAX
		self.reading_pipe=read_pipe
		self.writing_pipe=write_pipe
		self.reading_child=1
		self.radio = None
		
	def set_bit_rate(self,rate='1M'):
		if rate=='1M':
			self.data_rate=NRF24.BR_1MBPS
		elif rate=='2M':
			self.data_rate=NRF24.BR_2MBPS
		elif rate=='250K':
			self.data_rate=NRF24.BR_250KBPS
		else :	
			self.data_rate=NRF24.BR_1MBPS #default
	
	def set_ce_pin(self,ce_pin):
		self.ce_pin=ce_pin
		
				
	def start(self,crc_check=False):	
		try:
			self.radio = NRF24()
			self.radio.begin(self.spi_major,self.spi_minor,self.ce_pin,self.irq_pin)
			self.radio.setRetries(self.retrie_delay,self.retrie_times)
			self.radio.setPayloadSize(self.payload_size)
			self.radio.setChannel(self.channel)
			self.radio.setDataRate(self.data_rate)
			self.radio.setPALevel(NRF24.PA_MAX)			
			if crc_check == False:
				self.radio.disableCRC()
			self.radio.openWritingPipe(self.writing_pipe)
			self.radio.openReadingPipe(self.reading_child,self.reading_pipe)
			self.radio.startListening()
			self.radio.stopListening()
		except:
			self.radio=None	
			
   

		
	def send_msg(self,msg,to_addr=[]):
		if self.radio == None :
			return
		if to_addr != []  :
			self.radio.openWritingPipe(to_addr)	
		self.radio.stopListening()
		res=self.radio.write(msg)
		return res
		
		
	def get_msg(self,from_addr=[]):
		if self.radio == None :
			return
		if from_addr != []:	
			self.radio.openReadingPipe(self.reading_child,from_addr)	
		self.radio.startListening()	
		pipe=[1]
		while not self.radio.available(pipe):
			#block until there is a message come in
			time.sleep(1000/1000000.0)
		recv_buf= []        
		self.radio.read_payload(recv_buf,self.payload_size)
		out=''
		for c in recv_buf :
			out=out+ chr(c)
		return out
		
	def showDetails(self):
		if self.radio == None :
			return
		self.radio.printDetails()
			
	def close(self):
		if self.radio is None :
			return
		self.radio.end()		

