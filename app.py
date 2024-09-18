from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['1umi409xQu0avl0NjimOA50LtSOTSGqb5B514j6ckvllPETKaDXxfHxDTbv1+ESu9jE0Ubk+6fUSo+7Hgmke/iGs+W2gOQZ8rBTumMruBHICSOInRx8UXM1VKLeu6IHLNfUAjgzZNM9XBsp/51Y7fQdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['28be3a2737eb0717a909309116d7e861'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)