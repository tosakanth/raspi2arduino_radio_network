<h1>Radio Network for Raspberry PI and Arduino</h1>
To build a simple radio wireless network by using of <a href="http://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo">NRF24L01 Plus</a> module.



<h3>What you need to install on Raspberry PI before going on.</h3>
1. RPi.GPIO from https://pypi.python.org/pypi/RPi.GPIO
2. Py-spidev from https://github.com/doceme/py-spidev
I've modified original nrf24.py from https://github.com/jpbarraca/pynrf24/blob/master/nrf24.py to be suitable for Raspberry PI and RPi.GPIO.

<h3>Wiring </h3>
This may be changed depends on your Arduino Model.

<img src="http://arduino-info.wikispaces.com/file/view/24L01Pinout-800.jpg/243330999/24L01Pinout-800.jpg">

<table align="center">
<tr><th>NRF24L01 Plus</th><th>Arduino Mega 2560</th></tr>
<tr><td>VCC</td><td>3.3V</td></tr>
<tr><td>GRD</td><td>GRD</td></tr>
<tr><td>CE</td><td>9</td></tr>
<tr><td>CSN</td><td>10</td></tr>
<tr><td>SCK</td><td>52</td></tr>
<tr><td>MOSI</td><td>51</td></tr>
<tr><td>MISO</td><td>50</td></tr>
<tr><td>IRQ</td><td>No use</td></tr>
</table>

<table align="center">
<tr><th>NRF24L01 Plus</th><th>Raspberry PI</th></tr>
<tr><td>VCC</td><td>3.3V (pin 1)</td></tr>
<tr><td>GRD</td><td>GRD (pin 6)</td></tr>
<tr><td>CE</td><td>GPIO 25 (pin 22)</td></tr>
<tr><td>CSN</td><td>GPIO 8 (pin 24)</td></tr>
<tr><td>SCK</td><td>GPIO 11 (pin 23)</td></tr>
<tr><td>MOSI</td><td>GPIO 10 (pin 19)</td></tr>
<tr><td>MISO</td><td>GPIO 9 (pin 21)</td></tr>
<tr><td>IRQ</td><td>GPIO 18 (pin 12)</td></tr>
</table>
