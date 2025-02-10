import os
import google.generativeai as genai

# help(genai)

os.environ["GOOGLE_API_KEY"] = "AIzaSyBKy3gmAsRuYR-8fpdGClyVOZ4IuBoq6Es"


genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

try:

    response = model.generate_content(
        contents = [{"parts":[{"text": "מהן process?"}]}],
    )

    print(response.text)
except Exception as e:
    print(f"Error{e}")

print(type(response.text))

