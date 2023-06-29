# Define our theme color
alpaca_blue = '#066BAF'

def image_in_FlexMessage(url):
    return {"type": "image",
            "url": url,
            "size": "full",
            "aspect_ratio": "20:13",
            "aspect_mode": "cover"}

def text_in_FlexMessage(text, size, color, weight='regular', wrap=False):
    return {"type": "text",
            "text": text,
            "size": size,
            "color": color,
            "weight": weight,
            "wrap": wrap }

def logo_in_FlexMessage(text='PhoebeFlex'):
    return text_in_FlexMessage(text, size='md', color=alpaca_blue, weight='bold')

def title_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555', weight='bold')

def heading_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='xl', color='#555555')

def note_in_FlexMessage(text):
    return text_in_FlexMessage(text, size='md', color='#AAAAAA', wrap=True)

def separator_in_FlexMessage(margin='xl'):
    return {"type": "separator", "margin": margin}

def button_in_FlexMessage(label, data, display_text):
    return {"type": "button",
            "action": {
                "type": "postback",
                "label": label,
                "data": data,
                "display_text": display_text
            },
            "style": "link",
            "color": alpaca_blue,
            "height": "sm"}

def index_FlexMessage():
    hero_image_url = 'https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_2_restaurant.png'
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage('Into the alpaca_training'), 
                     separator_in_FlexMessage(), 
                     heading_in_FlexMessage('Overall'), 
                     note_in_FlexMessage('# 查詢所有資料'),
                     heading_in_FlexMessage('alpaca_name'), 
                     note_in_FlexMessage('# 按照 alpaca_name 查詢'),
#                      heading_in_FlexMessage('training'), 
#                      note_in_FlexMessage('# 按照 training 查詢'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Overall', '::', '查詢 Overall'),
                       button_in_FlexMessage('alpaca_name', ':alpaca_name', '查詢 alpaca_name')]
#                       button_in_FlexMessage('training', 'training')]
    FlexMessage = {'type': 'bubble',
                   'hero': image_in_FlexMessage(hero_image_url),
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

def column_FlexMessage(column_name, dataclip):
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage(f'Into the {column_name}'), 
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage(f"{i}", f":{column_name}='{i}':", f"查詢 {i}") for i in dataclip]
    FlexMessage = {'type': 'bubble',
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage

def number_FlexMessage(column_query):
    body_contents = [logo_in_FlexMessage(), 
                     title_in_FlexMessage(f'Into the number'), 
                     separator_in_FlexMessage(),
                     heading_in_FlexMessage('Last 1'), 
                     note_in_FlexMessage('# 查詢最後一筆資料'),
                     heading_in_FlexMessage('Last 10'), 
                     note_in_FlexMessage('# 查詢最後十筆資料'),
                     separator_in_FlexMessage()]
    footer_contents = [button_in_FlexMessage('Last 1', f":{column_query}:1:", f"查詢 {column_query} 最後一筆"),
                       button_in_FlexMessage('Last 10', f":{column_query}:10:", f"查詢 {column_query} 最後十筆")]
    FlexMessage = {'type': 'bubble',
                   'body': {
                       'type': 'box', 
                       'layout': 'vertical', 
                       'spacing': 'md', 
                       'contents':body_contents},
                   'footer': {
                       'type': 'box',
                       'layout': 'vertical',
                       'contents': footer_contents}}
    return FlexMessage