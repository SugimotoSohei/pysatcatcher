# -*- coding: utf-8 -*-

import unittest
import serial
import threading
import time

class RAC805:
    def __init__(self):
        #self._ser = serial.serial('/dev/tty',9600)
        pass
    def connect(self,port):
        self._ser = serial.Serial(port, 9600, timeout=0)

    def moveazel(self,az,el):
        if(el>=0.0):
            command = "AZ"+str(az)+" EL"+str(el)+"\r"
            self._ser.write(command)
        return True

    def stop(self):
        command = "\r"
        self._ser.write(command+"\r")
        return True

    def recieve(self):
        result=""
        while not((">>" in result) or ("" == result)):
        #while(False):
            print('recieve')
            time.sleep(0.0001)
            result=self._ser.readline()
            print(result)
        return True

    def close(self):
        self._ser.close()
        return True

class Antenna(object):
    def __init__(self,rotatormodel):
        if rotatormodel == "RAC805":
            self._radio = RAC805()
    def connect(self,port):
            self._radio.connect(port)
    def moveazel(self,az,el):
        return self._radio.moveazel(az,el)
    def stop(self):
        return self._radio.stop()
        
    def recieve(self):
        self._radio.recieve()
        #t=threading.Thread(target=self._radio.recieve())
        #t.setDaemon(True)
        #t.start()
        #print "threadstart"
    def close(self):
        return self._radio.close()

