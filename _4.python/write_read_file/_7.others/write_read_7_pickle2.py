import pickle

print('使用 pickle 模組 寫讀二進位檔案')



import pickle
game_info = {
    "position_X":"100",
    "position_Y":"200",
    "money":300,
    "pocket":["黃金", "鑰匙", "小刀"]
}

fn = "tmp_pickle.dat"
fn_obj = open(fn, 'wb')         # 二進位開啟
pickle.dump(game_info, fn_obj)
fn_obj.close()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
