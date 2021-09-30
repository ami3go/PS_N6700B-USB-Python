import logging
import datetime

def get_time_stamp():
    time_var = datetime.datetime.now()
    return(time_var.strftime("%y-%m-%d %H:%M:%S"))


def  get_file_name(txt=""):
    now = datetime.datetime.now()  # current date and time
    date_time_in_file_name = now.strftime("%Y_%m_%d__%H-%M-%S")  # get time and date formated into file friendly string
    file_path = "C:\\Users\\Vision\\Desktop\\JLR_CHCM\\logs\\"
    file_name_can_const = "_CHCM_PS_log.txt"  # fixed part of log file name
    file_name_can = file_path + date_time_in_file_name + "_" + txt  + file_name_can_const  # making a single string
    print("[Debug]: your CAN log file will be here -> ", file_name_can)  # just to check
    return file_name_can


class txt_logger:
    def __init__(self):
        self.app = None
        self.file_name = None
    def init(self, txt=""):
        self.app = logging.getLogger('CHCM_PSlog')
        self.file_name = get_file_name(txt)
        can_hdlr = logging.FileHandler(self.file_name)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        can_hdlr.setFormatter(formatter)
        self.app.addHandler(can_hdlr)
        self.app.setLevel(logging.INFO)  # set logging massage level

    def stop_logging(self, message=None):
        # self.app.flush()
        # self.app.close()
        if message is not None:
            print(f"{message} Log File location: {self.file_name}")  # just to check
        self.app = None
        self.file_name = None

    def print_and_log(self, txt):
        self.app.info(txt)
        # self.app.flush()
        print(get_time_stamp(), txt)

    def print_and_log_ml(self, multi_line_txt):
        for x in range(len(multi_line_txt)):
            self.print_and_log(multi_line_txt[x])

    def insert_blank_lines(self, line_num=1):
        for i in range(line_num):
            txt = ""
            self.print_and_log(txt)
