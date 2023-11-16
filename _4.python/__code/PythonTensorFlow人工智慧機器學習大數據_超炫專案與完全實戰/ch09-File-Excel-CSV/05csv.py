#!/usr/bin/env
# -*- coding: utf-8 -*-    
__author__ = "Powen Ko, www.powenko.com"

import csv
with open('workfile.csv', 'r') as fin:
    with open('write.csv', 'w') as fout:
        read = csv.reader(fin, delimiter=',')
        write = csv.writer(fout, delimiter=',')
        header = next(read)
        print(header)
        # get number of columns
        #array = header.split(',')
        first_item = header[0]
        write.writerow(header)
        for row in read:
            print(','.join(row))
            write.writerow(row)
            print(row[2])