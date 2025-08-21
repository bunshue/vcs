"""
sugar 安裝 pip install pyrebase==3.0.10

This Python command line app that uses Firebase authentication.
這個使用 Firebase 身份驗證的 Python 命令列應用程序。

1.
Register new users using email + password
使用電子郵件 + 密碼註冊新用戶
2.
Verify whether the email already belongs to a user
確認電子郵件是否已屬於使用者
3.
Sign in with email + password
使用電子郵件 + 密碼登入
4.
Keep track of the application's current user.
追蹤應用程式的目前使用者。
"""

import pyrebase

# Configure and Connext to Firebase

firebaseConfig = {
    "apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:59f51ba5b6a475032f2459",
    "measurementId": "G-TNR2V3DEQD",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# 註冊


def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask = input("Do you want to login?[y/n]")
        if ask == "y":
            login()
    except:
        print("Email already exists")
    return


# 登入


def login():
    print("Log in...")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login["idToken"]))
    # email = auth.get_account_info(login["idToken"])["users"][0]["email"]
    # print(email)
    except:
        print("Invalid email or password")
    return


# 主程式

ans = input("Are you a new user?[y/n]")

if ans == "n":
    login()
elif ans == "y":
    signup()


""" 已使用
Enter email: david@lion.mouse.com
Enter password: abc123
"""
