import facebook

token="EAACEdEose0cBAA2TXAUVh5cVoWP2lxg04k9ST3MZBd7UeOAC0KDS5xPNtZB4dlEQkUxNeiKfxZA4o4r7PSkrpUHByVai2ZC64eakYE301zakh7iGfKUkPr0YfsNwQLyiantM26pA0wVLrOuGBqufJVWVlD8aVuPYRCmvZBZAT6ZCAZDZD"
graph = facebook.GraphAPI(access_token=token,version='2.7')

pages = graph.get_connections(id='me', connection_name='posts')
posts = pages['data']

for p in posts:
    graph.put_like(p['id'])
    print (p['id'],"按讚成功!") 