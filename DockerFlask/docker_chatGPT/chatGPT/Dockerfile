FROM python:3.9

WORKDIR /app/Flask/chatGPT

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV OPENAI_API_KEY="your-openai_api_key"

EXPOSE 5000

CMD ["python3", "app.py"]
