# -*- coding: utf-8 -*-
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from modules import cbpi
from modules.core.hardware import  SensorActive
from modules.core.props import Property


@cbpi.sensor
class PHSensor(SensorActive):

    #channel = Property.Number("Channel", configurable=True, default_value=0)
    MCPchannel = (Property.Select("MCP3008 Channel", options=["0", "1", "2", "3", "4", "5", "6", "7"], description="Enter channel-number of MCP3008"))
    
    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        return " pH"

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
            cbpi.app.logger.info('PH Sensor channel     %s' % (ch))                     #debug
            
            #value = mcp.read_adc(0)                                                    #change MCP3008 channel here
            value= mcp.read_adc(int(ch))                                                #change MCP3008 channel here via propertys of sensor
            cbpi.app.logger.info('PH Sensor value     %s' % (value))                    #debug or calibration

            voltage = (5 / 1023.0 * value)
            cbpi.app.logger.info('PH Sensor voltage %.3f' % (voltage))                  #debug or calibration

            phvalue = ("%.2f" % (7 + ((2.532 - voltage) / 0.1839)))
            cbpi.app.logger.info("PH Sensor phvalue %s%s" % ((phvalue),("0")))          #debug or calibration
            
            self.data_received(phvalue)

            #mcp.close()
            
            self.api.socketio.sleep(2)
            

@cbpi.initalizer()
def init(cbpi):
    
    
    pass

