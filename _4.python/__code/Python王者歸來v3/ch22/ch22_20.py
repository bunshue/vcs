# ch22_20.py
import pickle

fn = "data19.dat"
fn_obj = open(fn, 'rb')         # 二進位開啟
game_info = pickle.load(fn_obj)
fn_obj.close()
print(game_info)









