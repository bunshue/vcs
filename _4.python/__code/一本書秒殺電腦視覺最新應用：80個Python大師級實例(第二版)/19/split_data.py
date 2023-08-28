import os
import random
import shutil
import numpy as np

def init_folder(fd):
    if os.path.exists(fd):
        shutil.rmtree(fd)
        os.makedirs(fd)
    else:
        os.makedirs(fd)

def mk_folder(fd):
    if os.path.exists(fd) is False:
        os.makedirs(fd)

def get_all_files(input_db):
    files_list = []
    sub_db_list = os.listdir(input_db)
    for sub_db in sub_db_list:
        input_dbi = input_db + '/' + sub_db + '/'
        files = [input_dbi + file for file in os.listdir(input_dbi)]
        files_list.extend(files)

    return files_list

def gen_db_folder(input_db):
    sub_db_list = os.listdir(input_db)
    rate = 0.8
    train_db = './train'
    test_db = './test'
    init_folder(train_db)
    init_folder(test_db)
    for sub_db in sub_db_list:
        input_dbi = input_db + '/' + sub_db + '/'
        train_dbi = train_db + '/' + sub_db + '/'
        test_dbi = test_db + '/' + sub_db + '/'
        mk_folder(train_dbi)
        mk_folder(test_dbi)
        fs = os.listdir(input_dbi)
        random.shuffle(fs)
        le = int(len(fs) * rate)
        for f in fs[:le]:
            shutil.copy(input_dbi + f, train_dbi)
        for f in fs[le:]:
            shutil.copy(input_dbi + f, test_dbi)

if __name__ == '__main__':
    gen_db_folder('./db')

