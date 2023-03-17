import sys
sys.dont_write_bytecode = True

import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

if not os.environ.get("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
openai.api_key = os.getenv("OPENAI_API_KEY")
model_list = openai.Model.list()
model_names = [model['id'] for model in model_list['data']]

@app.route("/", methods = ("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        model = request.form.get("menu")
        try:
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=1000,
                temperature=0.6,
            )
            result=response.choices[0].text
        except:
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                # access first JSON object returned, it's message, and then the contents of that message
                result=response.choices[0]["message"]["content"]
            except:
                print("Error, completion model not supported")
        return redirect(url_for("index", result=result,  model=model))

    result = request.args.get("result")
    return render_template("index.html", result=result, model_names=model_names)

# attempting to now add in chrome extension
@app.route("/completion", methods=["POST"])
def get_completion():
    data = request.get_json()
    prompt = data["prompt"]
    model = data["model"]

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=100,
        temperature=0.6,
    )

    print("Response object:", response)
    return jsonify({"result": response.choices[0].text})



