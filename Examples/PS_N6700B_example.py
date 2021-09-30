import src.PS_N6700B_class as power
import time
import src.Logging_class as logger

log_txt = logger.txt_logger()
log_txt.init("")
wait_time = 60
if __name__ == "__main__":
    try:
        ps = power.PS_N6700B_class()

        #gen.conf_puls()
        time.sleep(2)
        vout_1 = 12.000
        vout_2 = 12.000

        ps.set_voltage(vout_1, 1)
        ps.set_voltage(vout_2, 2)

        ps.set_current(5, 1)
        ps.set_current(5, 2)





        while True:
            log_txt.print_and_log(f"{power.get_time_stamp()}: Power ON")
            ps.set_output_on(1)
            # ps.set_output_on(2)
            current_1 = round(float(ps.measure_current_dc(1)),3)
            current_2 = round(float(ps.measure_current_dc(2)),3)
            log_txt.print_and_log(f"{power.get_time_stamp()} PS1: {current_1} A, PS2: {current_2} A")
            time.sleep(60)
            current_1 = round(float(ps.measure_current_dc(1)), 3)
            current_2 = round(float(ps.measure_current_dc(2)), 3)
            # print(f"PS1: {current_1} A, PS2: {current_2} A")
            log_txt.print_and_log(f"{power.get_time_stamp()} PS1: {current_1} A, PS2: {current_2} A")
            log_txt.print_and_log(f"{power.get_time_stamp()} : Power OFF, and wait: {wait_time} s")
            ps.set_output_off(1)
            # ps.set_output_off(2)
            time.sleep(wait_time)

    except KeyboardInterrupt:
        time.sleep(2)
        ps.set_output_off(1)
        ps.set_output_off(2)
        ps.close()