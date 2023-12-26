# ch32_6.py
import facebook

token = "EAAPGT8IPNwcBAHAU5QjYgyAw23bUinXqBpUZC8OU3VAeeWFK4clu7cA1KQ4pQHCZARofcGhctGML7itS7GPDehMFxG9lbSANtzXDC3UXrhzB7RX0OXaDj8bR1VhqWw6VxFSlDLlmuycMZBjrrFGPJbxZAdGQKTnQLhZBPKkCbMRZC5H2L5bt4V8Ur2cRSQlyFpIOdnX5D6ZCEXnVO4FAkza406TBRKogQckPl0swBo1UgZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.1')
mylikes = graph.get_connections(id='me',
                               connection_name='likes')

likes = mylikes['data']
print("按讚的社團數 : ", len(likes))
for like in likes:
    print(like['name'])




    













