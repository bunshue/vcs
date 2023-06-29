import datetime

import boto3
from boto3.dynamodb.conditions import Attr

import DBhardwork

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('memory')

today = str(datetime.datetime.today().date())
current = str(datetime.datetime.today())

def review():
    response = table.scan(
        FilterExpression=Attr('recordDate').eq(today),
        ProjectionExpression='target, recordDate'
    )
    items = response['Items']
    print(items)
    return items

def check(target):
    response = table.get_item(
        Key={'target': target}
    )
    print(response)
    
    if 'Item' in response:
        item = response['Item']
        print('item from memory:', item)
        target = item['target']
        title = item['title']
        item_key = [key for key in item.keys() if '_' in key]
        item_key = sorted(item_key)
        reply_dict = dict()
        for i in range(0, len(item_key), 3):
            pos_key = item_key[i]
            trans_key = item_key[i + 1]
            eng_key = item_key[i + 2]
            reply_dict[item[pos_key]] = [item[trans_key], item[eng_key]]
        return target, title, reply_dict
    else:
        return None
        
def save(target):
    print('datetime from dynamo:', current)
    response = table.get_item(
        Key={'target': target}
    )
    
    print('response', response)

    if 'Item' in response:
        # update
        table.update_item(
            Key={'target': target},
            UpdateExpression='SET recordDate = :val1',
            ExpressionAttributeValues={':val1': today}
        )
        
        return f'update {target}'
        
    else:
        target, title, reply_dict = DBhardwork.do_google_translate(target)

        item_from_dict = {'target': target, 'title': title, 'recordDate': today}
        for i, key in enumerate(reply_dict):
            item_from_dict[f'{i}_0_pos'] = key
            item_from_dict[f'{i}_1_trans'] = reply_dict[key][0]
            item_from_dict[f'{i}_2_eng'] = reply_dict[key][1]
            
        table.put_item(
            Item=item_from_dict
        )
        
        return f'save {target}'