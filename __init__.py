# -*- coding: utf-8 -*-
from MCP3008 import MCP3008
from modules import cbpi
from modules.core.hardware import  SensorActive
from modules.core.props import Property

@cbpi.sensor
class PHSensor(SensorActive):

    #channel = Property.Number("Channel", configurable=True, default_value=0)
    MCPchannel = Property.Select("Channel", options=["0", "1", "2", "3", "4", "5", "6", "7"], description="Enter channel-number of MCP3008")
    phvalue = 0

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
            try:
                adc = MCP3008()
                value = adc.read(channel = 0) #Den auszulesenden channel kann man anpassen
                #value = adc.read(channel = MCPchannel) 
                phvalue = (".2f" % (value / 1023.0 * 3.3))
                #phvalue = 5.33
                cbpi.app.logger.info('PH Sensor value %s' % (phvalue))
                #print("Anliegende Spannung: %.2f" % (value / 1023.0 * 3.3))
                self.data_received(phvalue)
            except:
                pass
            self.api.socketio.sleep(5)
            #time.sleep(5)

@cbpi.initalizer()
def init(cbpi):
    print "INITIALIZE HTTP SENSOR MODULE"
    #cbpi.app.register_blueprint(blueprint, url_prefix='/api/httpsensor')
    print "READY"
