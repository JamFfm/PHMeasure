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
    MCPchannel = Property.Select("MCP3008 Channel", options=["0", "1", "2", "3", "4", "5", "6", "7"], description="Enter channel-number of MCP3008")
    #phvalue = 0
    
    def get_unit(self):
        '''
        :return: Unit of the sensor as string. Should not be longer than 3 characters
        '''
        return "ph"

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
            #try:
            # Software SPI configuration:
            CLK  = 6
            MISO = 13
            MOSI = 19
            CS   = 26
            mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

            # Hardware SPI configuration:
            # SPI_PORT   = 0
            # SPI_DEVICE = 0
            # mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
            
            value = mcp.read_adc(0) #Den auszulesenden channel kann man anpassen
            voltage = (5 / 1023.0 * value)
            phvalue = ("%.2f" % (7 + ((2.5 - voltage) / 0.1839)))
            
            cbpi.app.logger.info('PH Sensor value %s' % (phvalue))
            
            self.data_received(phvalue)
            #mcp.close()
            #except:
            #    pass
            self.api.socketio.sleep(2)
            #time.sleep(5)

@cbpi.initalizer()
def init(cbpi):
    
    pass

