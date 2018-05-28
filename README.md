# PHMeasure
Craftbeerpi3 Sensor for phMeasure
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

sudo apt-get update

sudo apt-get install build-essential python-dev python-smbus git

cd ~

git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git

cd Adafruit_Python_MCP3008

sudo python setup.py install

or

use the Insatall file.

go to pi home/craftbeerpi3

than key in 

./install.sh
