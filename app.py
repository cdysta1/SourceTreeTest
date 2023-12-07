from flask import Flask, render_template, request
import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response


app = Flask(__name__)
apiKey = "pyjf4xwvrjAJt5TfZPMzXTZzbf9kPif50nPQdt1iiHA"


async def get_responses(api_key, prompt):
    message = ProtocolMessage(role="user", content=prompt)
    response = ''
    async for partial in get_bot_response(messages=[message], bot_name="Llama-2-70b", api_key=api_key):
    #处理服务器返回值: 是一个键值对，其中键为'text'的包含有效文本数据，全部汇总到response变量然后返回
      for key,value in partial:
        if key == 'text':
          response += value
          response = response.replace("\n", "<br>")
    return response


@app.route("/")
def init():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/chatbox")
def chatbox():
    return render_template("chatbox.html")


@app.route("/chatbox/input")
def input():
    name = request.args.get("name", "")
    print(name)
    serverMessage = asyncio.run(get_responses(apiKey, name))
    print(serverMessage)
    return serverMessage


if __name__ == '__main__':
    app.run(debug=True)
