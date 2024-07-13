import openai
import os

def GetResponse(text):
    try:
        api_key=os.environ.get("OPENAI_API_KEY")
        openai.api_key = api_key
        result = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=text,
            max_tokens=500,
            n=1
            )
        response = result["choices"][0]["text"]
        return response
    except Exception as exception:
        print(exception)
        return "error"