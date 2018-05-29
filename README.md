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

## or

## use the install.sh file:

install PHMeter as addon in Cbpi 3

open commandline

key in

cd /home/pi/craftbeerpi3/modules/plugins/PHMeasure/

than key in 

./install.sh

reboot Raspi

# calibation


## using potis


