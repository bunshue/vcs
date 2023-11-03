# F1750 練習 22

import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename, 'r') as f_read, \
            open(csv_filename, 'w', newline='') as f_write:
        csv_reader = csv.reader(f_read, delimiter=':')
        csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')
        for line in csv_reader:
            csv_writer.writerow([line[0], line[2]])

passwd_to_csv(r'.\data\passwd.cfg', r'.\data\passwd.csv')
