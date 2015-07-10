from nrf24 import NRF24
import time

class TK_RADIO:
	
	def __init__(self,spi_major=0,spi_minor=0,ce_pin=25,irq_pin=18,channel=90):
		
		self.spi_major=spi_major
		self.spi_minor=spi_minor
		self.ce_pin=ce_pin
		self.irq_pin=irq_pin
		self.retrie_delay=15 #15*250usec
		self.retrie_times=15 #retry 15 times
		self.payload_size=20 #max is 32
		self.channel=channel
		self.data_rate=NRF24.BR_1MBPS
		self.palevel=NRF24.PA_MAX
		self.child_pipes=[]
		self.time_out=3000 #3000 milli seconds
		self.radio = None
		

	def begin(self,crc_check=False):	
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
		except:
			self.radio=None	
	
	def set_payload_size(self,size=20):
		if size > 32 :
			size=32
		self.payload_size=size
		self.radio.setPayloadSize(self.payload_size)
					
	def set_bit_rate(self,rate='1M'):
		if rate=='1M':
			self.data_rate=NRF24.BR_1MBPS
		elif rate=='2M':
			self.data_rate=NRF24.BR_2MBPS
		elif rate=='250K':
			self.data_rate=NRF24.BR_250KBPS
		else :	
			self.data_rate=NRF24.BR_1MBPS #default
	
	def set_channel(self,channel):
		self.channel= channel
		self.radio.setChannel(self.channel)
		
	def set_ce_pin(self,ce_pin):
		self.ce_pin=ce_pin
		
	def powerUp(self):
		if self.radio == None :
			return
		self.radio.powerUp()
						   
	def set_timeout(self,limit=3000):
		if limit < 3000:
			limit=3000
		self.time_out=limit
		
	def send_msg(self,msg,to_addr=[]):
		if self.radio == None :
			return
		if to_addr != []  :
			self.radio.openWritingPipe(to_addr)	
		self.radio.stopListening()
		res=self.radio.write(msg)
		return res
		
	
	def openReadingPipes(self,addr_list=[]):
		#you can open 5 pipes at the same time for reading data.
		if self.radio == None :
			return
		if len(addr_list)<1 :
			return	
		cpipe=1
		for addr in addr_list :
			if cpipe < 6 :
				self.radio.openReadingPipe(cpipe,addr)	
				self.child_pipes.append(cpipe)
				cpipe=cpipe+1
	
		
	def get_msg(self):
		if self.radio == None :
			return None
		if len(self.child_pipes)<1:
			return None
		recv_buf= []        
		self.radio.startListening()	
		tick =0;
		while not self.radio.available(self.child_pipes) and (tick < self.time_out):
			#block until there is a message come in
			time.sleep(1000/1000000.0) # sleep for 1 millisec.
			tick = tick+1
			
		if tick < self.time_out	 :					
			self.radio.read_payload(recv_buf,self.payload_size)
			
		return recv_buf
			
		
	def showDetails(self):
		if self.radio == None :
			return
		self.radio.printDetails()
			
	def close(self):
		if self.radio is None :
			return
		self.radio.end()		
