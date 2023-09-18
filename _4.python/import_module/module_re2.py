import sys

import re

'''
def multiply(m):
    v = int(m.group())
    return str(v * 2)

def getVid(url):
    string strRegex = "(?<=id_)(\\w+)";
    Regex reg = new Regex(strRegex);
    Match match = reg.Match(url);
    return match.ToString();


print("正規表示式的使用")
url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
vid = getVid(url);
print("vid : " + vid)


print("取得email帳號")

#取得email帳號

senderEmail = @"david@insighteyes.com";
string[] sendFromUser = senderEmail.Split('@');
int len = sendFromUser.Length;
print("len = " + len.ToString())
int i;
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + sendFromUser[i])
}


print("用Regular Expression拆解e-mail帳號")

List<string> emailList = new List<string>();
email = "xue@163.,xue@163.com12,2707@qq.com,,xue@yahoo.com.cn,xue@163.com,xue@163.com12";
#  Regex reg2 = new Regex(@"^\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,}$");驗證email的正則表達式  

Regex reg = new Regex(@"(?<email>[\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,})");
Match m = reg.Match(email);
foreach (Match item in reg.Matches(email))
{
emailList.Add(item.Groups["email"].Value);
}
len = emailList.Count;
print("共取得 : " + len.ToString() + " 個帳號")
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + emailList[i])
}
'''

print("正規表示式的使用")

'''
text = 'tem12po'
pattern = r'[a-z]+'
txt = re.match(pattern, text)
print(txt.group()) # <re.Match object; span=(0, 3), match='tem'>
'''

#正規表示式的使用

#正規表示式

#使用方法
#Regex.Match("String", @"正規表示式").ToString();

text = "USA stands for the United States of America with 50 states and 330 millions people.";

#text = 'tem12po'
#pattern = r'[a-z]+'
#txt = re.match(pattern, text)
#print(txt) # <re.Match object; span=(0, 3), match='tem'>


#只提出字串最前面或最後面的英文
pattern = r"[A-Z]+"
txt = re.match(pattern, text)
print("結果 : ", txt.group())

#只提出字串最前面或最後面的數字
pattern = r"[\d_]+"
txt = re.match(pattern, text)
print("ddd結果 : ", txt)

#其他規則
text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)   #Output:"ABC456"
print("ddd結果 : ", txt)

text = "123ABC456DeF"
pattern = r"[0-9A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456D"
print("結果 : ", txt.group())

text = "123ABC456DeF"
pattern = r"[0-9A-Za-z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123D"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("ddd結果 : ", txt)

text = "123ABC"
pattern = r"\d"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group(), "\t數字")

text = "ABC 123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456-DeF"
pattern = r"[0-9A-Za-z\-]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())


print("檢查台灣手機號碼")
'''
text = "0922123456";

print("Text = " + text)
bool match;
match = System.Text.RegularExpressions.Regex.IsMatch(text, @"^09[0-9]{8}$");
if (match == true)
{
print("OK")
}
else
{
print("NG")
}


print("檢查中國手機號碼")

text = "13987654321";

print("Text = " + text)

if (!IsHandset(text))
{
print("NG")
}
else
{
print("OK")
}

print("檢查是否為數值")

text = "0x1234";

print("Text = " + text)

if (Regex.IsMatch(text, @"^[\d,\.]+$"))
{
print("是數值")
}
else
{
print("不是數值")
}
'''

