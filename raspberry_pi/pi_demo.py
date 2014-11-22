from nrf24_wrapper import *
import time

radio = P2PNetwork()
radio.start()
radio.showDetails()
msg='1234567890'
try:
  while True:
    radio.send_msg(msg)
    reply=radio.get_msg()
    print reply
    time.sleep(0.5)
except KeyboardInterrupt :
  radio.close()
