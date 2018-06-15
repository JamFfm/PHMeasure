# -*- coding: utf-8 -*-
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from modules import cbpi
from modules.core.hardware import  SensorActive
from modules.core.props import Property


@cbpi.sensor
class PHSensor(SensorActive):

    MCPchannel = Property.Select("MCP3008 Channel", options=["0", "1", "2", "3", "4", "5", "6", "7"], description="Enter channel-number of MCP3008")
    sensorType = Property.Select("Data Type", options=["pH Value", "Voltage", "Digits"], description="Select which type of data to register for this sensor")
    # Use Data Types Voltage and Digits (MCP3008) for calibration

    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        if self.sensorType == "pH Value":
            return " pH"
        elif self.sensorType == "Voltage":
            return " V"
        elif self.sensorType == "Digits":
            return " Bit"
        else:
            return "select Data Type"

    def stop(self):
        '''
        Stop the sensor. Is called when the sensor config is updated or the sensor is deleted
        :return: 
        '''
        pass

    def execute(self):
        '''
        Active sensor has to handle its own loop
        :return: 
        '''
        while self.is_running():
            # Software SPI configuration (use the BCM GPIO PINS):
            CLK  = 6
            MISO = 13
            MOSI = 19
            CS   = 26
            mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

            # Hardware SPI configuration:
            # SPI_PORT   = 0
            # SPI_DEVICE = 0
            # mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

            
            ch = (self.MCPchannel)
            #cbpi.app.logger.info('PH Sensor channel     %s' % (ch))                     #debug
            
            value= mcp.read_adc(int(ch))                                                #change MCP3008 channel here via propertys of sensor
            #cbpi.app.logger.info('PH Sensor value     %s' % (value))                    #debug or calibration

            voltage = (5 / 1023.0 * value)
            #cbpi.app.logger.info('PH Sensor voltage %.3f' % (voltage))                  #debug or calibration

            phvalue = ("%.2f" % (7 + ((2.532 - voltage) / 0.1839)))
            #cbpi.app.logger.info("PH Sensor phvalue %s%s" % ((phvalue),("0")))          #debug or calibration

            if self.sensorType == "pH Value":
                reading = phvalue
            elif self.sensorType == "Voltage":
                reading = "%.3f" % (voltage)
            elif self.sensorType == "Digits":
                reading = value
            else:
                pass
            
            self.data_received(reading)

            #mcp.close()                                                                 #did not use this one, in case the CBPi stopps after a while use this lise. I did mir need i            
            
            self.api.socketio.sleep(3)
            

@cbpi.initalizer()
def init(cbpi):
    
    
    pass

