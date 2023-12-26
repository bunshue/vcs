# ch22_19.py
import pickle
game_info = {
    "position_X":"100",
    "position_Y":"200",
    "money":300,
    "pocket":["黃金", "鑰匙", "小刀"]
}

fn = "data19.dat"
fn_obj = open(fn, 'wb')         # 二進位開啟
pickle.dump(game_info, fn_obj)
fn_obj.close()







