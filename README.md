<h1>Radio Network for Raspberry PI and Arduino</h1>
To build a simple radio wireless network by using of <a href="http://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo">NRF24L01 Plus</a> module.

<h3>Wiring </h3>
This may be changed depends on your Arduino Model.<br/>

<img src="http://arduino-info.wikispaces.com/file/view/24L01Pinout-800.jpg/243330999/24L01Pinout-800.jpg">
<br/>
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
<br/>
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

<h3>What you need to install on Raspberry PI before going on.</h3>
1. RPi.GPIO from https://pypi.python.org/pypi/RPi.GPIO
2. Py-spidev from https://github.com/doceme/py-spidev
<b>Note</b> : I've modified original nrf24.py from https://github.com/jpbarraca/pynrf24/blob/master/nrf24.py to be suitable for Raspberry PI (originally designed for Beaglebone Black) and RPi.GPIO (originally utilizes Adafruit_BBIO.GPIO) .

<h3>Install Arduino's library</h3>
There are a few NRF24L01 libraries available but I have not found the differences among them and I prefer to use from maniacbug. Get the library from <a href="https://github.com/maniacbug/RF24">here</a> and intall it to your Arduino IDE (visit <a href="http://arduino-info.wikispaces.com/Arduino-Libraries">here</a> if you do not know how to install libraries).

<h3>To test them all</h3>
1. Prepare your devices and wire them all.
2. Down load all python files, put them somewhere on your Raspberry PI.
3. Compile and flash Arduino sketch.
4. on Raspberry PI type sudo python pi_demo.py
5. See the result.
 
