from app import handler
from app.custom_models import PhoebeTalks, PhoebeRichMenu

from linebot.models import MessageEvent, PostbackEvent
from linebot.models import TextMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_text(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        if not reply:
            reply = PhoebeTalks.query_record(event)
        
        if not reply:
            reply = PhoebeTalks.insert_record(event)
            
        if not reply:
            reply = PhoebeTalks.isch_reply(event)
            
        if not reply:
            reply = PhoebeTalks.pretty_echo(event)
            
@handler.add(PostbackEvent)
def handle_postback(event):
    print(event)
    query = event.postback.data
    phase = query.count(':')
    if query.startswith('RichMenu'):
        if phase == 1:
            PhoebeRichMenu.rich_menu_i(event)
        elif phase == 2:
            PhoebeRichMenu.rich_menu_ii(event)
    else:
        if phase == 1:
            PhoebeTalks.query_record_i(event)
        elif phase == 2:
            PhoebeTalks.query_record_ii(event)
        elif phase == 3:
            PhoebeTalks.query_record_iii(event)
        
PhoebeRichMenu.initialize_rich_menu()