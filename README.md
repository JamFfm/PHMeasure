# PHMeasure
Craftbeerpi3 sensor for phMeasure
this is alpha version. Do not use.
Most helpful links:
- https://forum.arduino.cc/index.php?topic=336012.0

and

- https://tutorials-raspberrypi.de/wp-content/uploads/2016/10/Raspberry-Pi-Gas-Sensor-MQ2-Steckplatine.png last post


  voltage = 5 / 1024.0 * measure; //classic digital to voltage conversion


  // PH_step = (voltage@PH7 - voltage@PH4) / (PH7 - PH4)


  // PH_probe = PH7 - ((voltage@PH7 - voltage@probe) / PH_step)


  phvalue = 7 + ((2.5 - voltage) / 0.18)
   
  
# How to connect

![Test Graph](https://github.com/JamFfm/PHMeasure/blob/master/RaspberryPiPHSensorSteckplatine.png "wireing")

# How to Install

## console

Key in each line

(1) sudo apt-get update

(2) sudo apt-get install build-essential python-dev python-smbus git

(3) cd ~

(4) git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git

(5) cd Adafruit_Python_MCP3008

(6) sudo python setup.py install

install PHMeter as addon in Cbpi 3

### or

## use the install.sh file:

install PHMeter as addon in Cbpi 3

open commandline

key in

cd /home/pi/craftbeerpi3/modules/plugins/PHMeasure/

than key in 

./install.sh

reboot Raspi

# Board description

![Test Graph](https://github.com/JamFfm/PHMeasure/blob/master/1.0x0.jpg "powerampfilter")



* BNC plug: Where you put the probe. It seems to work with any probe with a calibration difference.

* Pin To: Should be the temperature but I can't make it works.
* Pin Do: High/Low 3.3v adjustable limit.
* Pin G/GND: Probe ground. It may be useful when the ground is not the same as your Raspi. In fact I use the ground of the Raspi.
  In some circumstances the ground voltage of the liquid to measure can be different.
* Pin G/GND: Power ground (ex. Raspi).
* Pin V+/VCC: Input power 5V DC (direct from Raspi).
* Blue potentiometer close to BNC: pH offset.
* Blue potentiometer close to pins: limit adjustment.
* Black component with 103 printed (not the one between potentiometers): thermistor for temperature compensation.

# Calibration

## The offset

The offset is the shifting of all pH values to a specific voltage range. If a pH 7 output a voltage of 2.2v and pH 8 a voltage of 2.1v, then a shift of +0.3v move the pH 7 to 2.5v and the pH 8 to 2.4v. 


This can be done on the board or via software but it's probably easyer on the board because it's probe independant and there are less programming to do.


Connect GND (both) and Vcc to Raspi GND and 5v. Please use a levelshifter to avoid damage at the GPIO which only support 3.3v. 

Remove the probe and do a short circuit between the the small BNC hole and the external part of BNC. 

Put a voltmeter to measure the voltage between GND and Po. Adjust the pot (close BNC) until the output is 2.5v. 

Now the pH 7 have an exact value of 2.5v (511 with analogRead function) because the probe will output 0 millivolt.

## The steps

Now you need one or more buffer solutions depending the range and precision you want. Ideally you should know the range of the measure you want to do with your system. 

I use water (upcoming beer) between pH 5 and pH 7, then I choose the buffer 4.01 (and 6.86 to verify my stuff). If you usually measure pH between 8 and 10 choose buffer 9.18 (eventually 6.86 also).


Connect the (clean) probe and put it in the buffer then let it stabilize for a minute. You know it's stable when it goes up and down (3.04 then 3.05 then 3.03 then 3.04). Take note of the voltmeter value, in my example it's 3.05v.

## Unit per step

The PH_step calculation is quite simple. You take the difference between the two known voltage, in my example 2.5v@pH7 and 3.05v@pH4.01 which is -0.55v. 

It's the voltage range equivalent of the pH range from 7 to 4.01, which is 2.99 pH units. A small division of the voltage by pH units gives you a volts per pH number (0,1839... in my case).

The PH_probe is calculated by taking the known pH 7 voltage (2.5v) where we add some PH_step to match the probe voltage. This means that a pH of 8 have a voltage value of 2.5v (pH 7) + 0.1839 (1 unit/step); pH 9 then is 2.5v + 0.1839 + 0.1839 = 2.87v.



