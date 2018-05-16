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
