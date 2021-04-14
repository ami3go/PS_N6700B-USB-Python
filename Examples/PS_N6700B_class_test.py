import PS_N6700B_class
import time


ps = PS_N6700B_class.PS_N6700B_class()

#gen.conf_puls()
time.sleep(2)
vout = 2.000
ps.set_output_on(1)
ps.set_output_on(2)
ps.set_voltage(vout)
ps.set_voltage(vout, 2)
for i in range(0,300):
    vout = round((vout + 0.05),3)
    print(f"Vout: {vout}, Iout: {ps.measure_current_dc(2)}")

    ps.set_voltage(vout)
    ps.set_voltage(vout -1,2)
    time.sleep(0.5)



# vout = 0.00
# voltage_step = 0.1
# Vout_high = 6
# Vout_low = 3
# vout = Vout_low
# Nreps = 10
# step_delay = 0.5
# for x in range(0,Nreps ):
#     for v in range(round((Vout_high-Vout_low)/voltage_step)):
#         ps.set_voltage(vout)
#         ps.set_voltage(vout,2)
#         time.sleep(step_delay)
#         vout = round((vout + voltage_step),3)# function round should be used beca
#     for v in range(round((Vout_high-Vout_low)/voltage_step)):
#         ps.set_voltage(vout)
#         ps.set_voltage(vout, 2)
#         time.sleep(step_delay)
#
#         vout = round((vout - voltage_step), 3)

time.sleep(2)
ps.set_output_off()
ps.set_output_off(2)
ps.close()