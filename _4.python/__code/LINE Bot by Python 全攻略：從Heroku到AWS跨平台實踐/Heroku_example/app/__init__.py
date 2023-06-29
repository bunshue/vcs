from flask import Flask
from flask_login import LoginManager
from linebot import LineBotApi, WebhookHandler
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

app.secret_key = config.get('flask', 'secret_key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.login_message = '請證明你並非來自黑暗草泥馬界'

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

from app import routes, models_for_line, models_for_login