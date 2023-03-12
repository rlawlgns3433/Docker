from flask import Flask, request, render_template
import openai
import os

# OpenAI API key
openai.api_key = "your-openai-api-key"

# Flask app
app = Flask(__name__)

# Root route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input
        user_input = request.form["user_input"]

        # Call OpenAI's GPT-3 API to generate response
        prompt = f"User: {user_input}\nAI:"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Format response and return to user
        message = response.choices[0].text.strip()
        return render_template("index.html", message=message, user_input=user_input)

    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
