import datetime

def word_flex_card(target, title, reply_dict, source, message_id):
    today = datetime.datetime.today()
    print('datetime from flex:', today)
    def vertical_box_content(text, size, color, weight="regular", margin=None, wrap=True):
        temp = {"type": "text",
                "text": text,
                "size": size,
                "color": color,
                "weight": weight,
                "wrap": wrap}
        if margin:
            temp["margin"] = margin
        return temp

    def horizontal_box_content(key, value, color, size):
        return {"type": "box",
                "layout": "horizontal",
                "contents": [{"type": "text",
                              "text": key,
                              "size": size,
                              "color": color,
                              "flex": 0},
                             {"type": "text",
                              "text": value,
                              "size": size,
                              "color": color,
                              "align": "end"}]}

    def separator(margin="xxl"):
        return {"type": "separator",
                "margin": margin}
                
    def button(label, data, display_text):
        return {
            "type": "button",
            "action": {
                "type": "postback",
                "label": label,
                "data": data,
                "display_text": display_text
            },
            "style": "link",
            "height": "sm",
            "color": "#982426"
        }

    def mega_content(reply_dict):
        mega_list = list()

        for pos, definitions in reply_dict.items():

            mega_list.append(vertical_box_content(pos, "md", "#cf73bd"))
        
            for trans, eng in zip(definitions[0], definitions[1]):
                mega_list.append(vertical_box_content(trans, "sm", "#666666"))
                mega_list.append(vertical_box_content(eng, "sm", "#aaaaaa"))

            mega_list.append(separator())

        return mega_list

    # reply_json = json.dumps(reply_dict, ensure_ascii=False)
    # print(str(reply_json))
    return {"type": "bubble",
            "body": {"type": "box",
                     "layout": "vertical",
                     "contents": [vertical_box_content("Greetings from D.B.", "sm", "#fc8162", "bold"), 
                                  vertical_box_content(target, "xxl", "#111111", "bold", margin="md"), 
                                  vertical_box_content(title, "md", "#aaaaaa", "bold"), 
                                  separator("md")] + 
                                  mega_content(reply_dict) +
                                 [horizontal_box_content("SEARCH IN", source, "#cccccc", "xs"),
                                  horizontal_box_content("MESSAGE ID", message_id, "#cccccc", "xs"),
                                  horizontal_box_content("DATETIME", str(today), "#cccccc", "xs"), 
                                  button('一鍵儲存', f'save:{target}', f'一鍵儲存 {target}'), 
                                  button('一鍵複習', 'review:', f'一鍵複習')]},
            "styles": {"footer": {"separator": True}}}
            
def review_flex_card(items):
    def vertical_box_content(text, size, color, weight="regular", margin=None, wrap=True):
        temp = {"type": "text",
                "text": text,
                "size": size,
                "color": color,
                "weight": weight,
                "wrap": wrap}
        if margin:
            temp["margin"] = margin
        return temp

    def horizontal_box_content(key, value, color, size):
        return {"type": "box",
                "layout": "horizontal",
                "contents": [{"type": "text",
                              "text": key,
                              "size": size,
                              "color": color,
                              "flex": 0},
                             {"type": "text",
                              "text": value,
                              "size": size,
                              "color": color,
                              "align": "end"}]}

    def separator(margin="xxl"):
        return {"type": "separator",
                "margin": margin}

    today = items[0]['recordDate']
    
    return {"type": "bubble",
            "body": {"type": "box",
                     "layout": "vertical",
                     "contents": [vertical_box_content("Greetings from D.B.", "sm", "#fc8162", "bold"), 
                                  vertical_box_content('Review', "xxl", "#111111", "bold", margin="md"), 
                                  vertical_box_content(today, "md", "#aaaaaa", "bold"), 
                                  separator("md")] + 
                                 [vertical_box_content(item['target'], 'sm', '#666666') for item in items]},
            "styles": {"footer": {"separator": True}}}