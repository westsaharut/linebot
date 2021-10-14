#LINE BOT
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi(
    'QFjde+bwUq1VmtSqbDHkMktNH1Y1LagDdCmBahiWGgSFXtUocKB6cdBsyGwHQ6fWI/kx8KGudyKcdbQZ3PjtcX55W8elt9i0tIgscgqjA1azx7Qt9aAR3sPfbU4qRxmdAH/vqfmklVPDl1qVBZ29xwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('360cdba78489a7e9c819e093e9b989d6')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Hello World! WZA'))
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='HII2! WZA'))
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Test Message! WZA'))


if __name__ == "__main__":
    app.run()
    print('BOOM')
