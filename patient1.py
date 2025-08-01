import os # operating system

# Controller using OOPS
class FileHelper:
    
    def __init__(self):
        
        patient_file_path = 'patient-log.csv'

        if os.path.exists(patient_file_path):
            print('FileHelper Initialized')
        else:
            file = open('patient-log.csv', 'a')
            headers = 'serial_no,date_time_stamp,name,phone,address,email,weight,height\n'
            file.write(headers)
            print('FileHelper Initialized for the First Time')

    def write_in_file(self, content):
        file = open('patient-log.csv', 'a')
        file.write(content)
        print('Content:', content, 'Saved in File')

    def read_file(self):
        file = open('patient-log.csv', 'r')
        lines = file.readlines()
        print('Reading Data From File. Total Lines:', len(lines))
        for line in lines:
            print(line)

    def file_size(self):
        file = open('patient-log.csv', 'r')
        data = file.read()
        return len(data)
    
    def lines_in_file(self):
        file = open('patient-log.csv', 'r')
        lines = file.readlines()
        return len(lines)