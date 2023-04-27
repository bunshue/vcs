pieSeries = [
{"name":"112/03/13","data":[{"name":"98 無鉛汽油","y":32.7,"GroupID":7}]},
{"name":"112/03/20","data":[{"name":"98 無鉛汽油","y":32.4,"GroupID":6}]},
{"name":"112/03/27","data":[{"name":"98 無鉛汽油","y":31.9,"GroupID":5}]},
{"name":"112/04/03","data":[{"name":"98 無鉛汽油","y":32.4,"GroupID":4}]},
{"name":"112/04/10","data":[{"name":"98 無鉛汽油","y":33.0,"GroupID":3}]},
{"name":"112/04/17","data":[{"name":"98 無鉛汽油","y":33.3,"GroupID":2}]},
{"name":"112/04/24","data":[{"name":"98 無鉛汽油","y":33.1,"GroupID":1}]},
{"name":"112/03/13","data":[{"name":"95 無鉛汽油","y":30.7,"GroupID":7}]},
{"name":"112/03/20","data":[{"name":"95 無鉛汽油","y":30.4,"GroupID":6}]},
{"name":"112/03/27","data":[{"name":"95 無鉛汽油","y":29.9,"GroupID":5}]},
{"name":"112/04/03","data":[{"name":"95 無鉛汽油","y":30.4,"GroupID":4}]},
{"name":"112/04/10","data":[{"name":"95 無鉛汽油","y":31.0,"GroupID":3}]},
{"name":"112/04/17","data":[{"name":"95 無鉛汽油","y":31.3,"GroupID":2}]},
{"name":"112/04/24","data":[{"name":"95 無鉛汽油","y":31.1,"GroupID":1}]},
{"name":"112/03/13","data":[{"name":"92 無鉛汽油","y":29.2,"GroupID":7}]},
{"name":"112/03/20","data":[{"name":"92 無鉛汽油","y":28.9,"GroupID":6}]},
{"name":"112/03/27","data":[{"name":"92 無鉛汽油","y":28.4,"GroupID":5}]},
{"name":"112/04/03","data":[{"name":"92 無鉛汽油","y":28.9,"GroupID":4}]},
{"name":"112/04/10","data":[{"name":"92 無鉛汽油","y":29.5,"GroupID":3}]},
{"name":"112/04/17","data":[{"name":"92 無鉛汽油","y":29.8,"GroupID":2}]},
{"name":"112/04/24","data":[{"name":"92 無鉛汽油","y":29.6,"GroupID":1}]}
];

print(type(pieSeries))

print()

print(len(pieSeries))

for info in pieSeries:
    #print(info)
    print('日期:', info['name'])
    #print(info['data'])
    for infos in info['data']:
        print('油品:', infos['name'])
        print('價格:', infos['y'])

'''
    
    for data in item['data']:
        if(data['name'] == '超級/高級柴油'):
            new_line = 0
            continue
        else:
            new_line = 1
        print("date:" + item['name'])   #第一層的 name 為日期
        print(data['name'] + ":" + str(data['y']))  #後面再接一層 array data 其中的 name 為產品名, 而 y 為單價
    if (new_line == 1):
        print("================")
'''

