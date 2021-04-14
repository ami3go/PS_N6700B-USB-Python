import sys
import pyvisa # PyVisa info @ http://PyVisa.readthedocs.io/en/stable/
import time

# https://www.keysight.com/upload/cmc_upload/All/34410A_Quick_Reference.pdf

## Number of Points to request
USER_REQUESTED_POINTS = 1000
    ## None of these scopes offer more than 8,000,000 points
    ## Setting this to 8000000 or more will ensure that the maximum number of available points is retrieved, though often less will come back.
    ## Average and High Resolution acquisition types have shallow memory depth, and thus acquiring waveforms in Normal acq. type and post processing for High Res. or repeated acqs. for Average is suggested if more points are desired.
    ## Asking for zero (0) points, a negative number of points, fewer than 100 points, or a non-integer number of points (100.1 -> error, but 100. or 100.0 is ok) will result in an error, specifically -222,"Data out of range"

## Initialization constants
SCOPE_VISA_ADDRESS = 'USB0::0x0957::0x0907::MY43014421::0::INSTR' # Get this from Keysight IO Libraries Connection Expert
    ## Note: sockets are not supported in this revision of the script (though it is possible), and PyVisa 1.8 does not support HiSlip, nor do these scopes.
    ## Note: USB transfers are generally fastest.
    ## Video: Connecting to Instruments Over LAN, USB, and GPIB in Keysight Connection Expert: https://youtu.be/sZz8bNHX5u4

GLOBAL_TOUT =  10 # IO time out in milliseconds

def range_check(val, min, max, val_name):
    if val > max:
        print(f"Wrong input value: {val_name}: [{val}]. Max value should be {max} ")
        print(f"Entered value: [{val}]  will be adjusted to {max} ")
        val = max
    if val < min:
        print(f"Wrong input value: {val_name}: [{val}]. Min value should be {min}")
        print(f"Entered value: [{val}]  will be adjusted to {min} ")
        val = min
    return val



class PS_N6700B_class:
    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        self.app = self.rm.open_resource(SCOPE_VISA_ADDRESS)
        IDN = str(self.app.query("*IDN?"))
        print(f': Connected to: {IDN}')
        ## Set Global Timeout
        ## This can be used wherever, but local timeouts are used for Arming, Triggering, and Finishing the acquisition... Thus it mostly handles IO timeouts
        self.app.timeout = GLOBAL_TOUT

        ## Clear the instrument bus
        self.app.clear()

    def set_voltage(self, voltage, channel_num=1):
        voltage = range_check(voltage, 0, 60, "Voltage")
        channel_num = range_check(channel_num, 1, 4, "PS Channel")
        self.app.write(f"VOLTage:LEVel:IMMediate:AMPLitude {voltage}, (@{channel_num})")

    def set_current(self, current, channel_num=1):
        current = range_check(current, 0, 5, "Voltage")
        channel_num = range_check(channel_num, 1, 4, "PS Channel")
        self.app.write(f"SOURce:CURRent:LEVel:IMMediate:AMPLitude {current}, (@{channel_num})")


    def set_output_on(self, channel_num=1):
        channel_num = range_check(channel_num, 1, 4, "PS Channel")
        self.app.write(f"OUTPut ON, (@{channel_num})")

    def set_output_off(self,channel_num=1):
        channel_num = range_check(channel_num, 1, 4, "PS Channel")
        self.app.write(f"OUTPut OFF, (@{channel_num})")

    def measure_current_dc(self,channel_num=1):
        channel_num = range_check(channel_num, 1, 4, "PS Channel")
        return_val = self.app.query(f"MEASure:SCALar:CURRent:DC? (@{channel_num})")
        return return_val

    def cmd_write(self, txt_cmd):
        self.app.write(txt_cmd)

    def cmd_query(self, txt_cmd):
        return_val = self.app.query(txt_cmd)
        return return_val

    def cmd_read(self):
        txt_cmd = "READ?"
        tmp = self.cmd_query(txt_cmd)
        return tmp


    def close(self):
        self.app.clear()
        self.app.close()