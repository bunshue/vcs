# ch32_3.py
import facebook

token = "EAAIZCihE7RSkBAAbuMKPfDXeCZABa8DHZBF3Arr4ZCgg62vy4cZA41Vz7SBzRLIjfnVJlgHhyIfr7MNnrXOUCQ4LrdJ841mNI600UBLS5qJAMMrXkcHZAnCvj9vZAKmGQE4DeSnWLN1UZBDsX1RYVLxXoikMuZAndv0gxGKoKumN4oJcPmI4RjKgWo5oDDIJf4fCrjphCy8VMwwZDZD"
graph = facebook.GraphAPI(access_token=token, version='3.1')

mypost = graph.get_object(id='1116138285252667_1113470975519398')
print("列出發文資料型態 : ", type(mypost))
print("列出發文資料內容 : ", mypost)
print("發文日期 : ", mypost['created_time'])
print("發文內容 : ", mypost['message'])
print("發文的id : ", mypost['id'])













