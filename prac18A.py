
import os
class Filehelper:
    def __init__(self):
        visitor_file_path = 'visitor-log.csv'

        if os.path.exists(visitor_file_path):
            print('filehelper initialized')
        else:
            file = open('visitor-log.csv','a')
            headers = ('serial_no,date_time_stamp,name,phone,address,whom_to_meet,purpose\n')
            file.write(headers)
            print('Filehepler initialized for the first time')

    def write_in_file(self,content):
        file = open('visitor-log.csv','a')
        file.write(content)
        print('Content:',content,'Saved in file')

    def read_file(self):
        file = open('vistor-log.csv','r')
        lines = file.readlines()
        print('Reading data from the file.Total Lines:', len(lines))
        for line in lines:
            print(line)
    
    def file_size(self):
        file = open('visitor-log.csv','r')
        data = file.read()
        return len(data)
    
    def lines_in_file(self):
        file = open('visitor-log.csv','r')
        lines = file.readlines()
        return len(lines)
    

