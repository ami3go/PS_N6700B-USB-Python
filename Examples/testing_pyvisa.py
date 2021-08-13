import sys
import pyvisa
import time

rm = pyvisa.ResourceManager()
app = rm.open_resource("USB0::0x03EB::0x2065::Agilent_Technologies_N6700B_MY43014421_D.04.09::0::INSTR")
IDN = str(app.query("ID?"))
print(f': Connected to: {IDN}')

print(app.query("OUT?"))

app.write("OUT ON")
time.sleep(0.25)
print(app.query("OUT?"))
time.sleep(0.25)
app.write("ISET 10A")
time.sleep(2)
app.write("VSET 13.5V")
print(app.query("VSET?"))
time.sleep(2)
app.write("OUT OFF")
print(app.query("OUT?"))