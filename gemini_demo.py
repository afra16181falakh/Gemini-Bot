import google.generativeai as genai

genai.configure(api_key="AIzaSyCnpZo_LcCFzpGnE96SvxYHU0LhVAhkSKU")

model = genai.GenerativeModel('gemini-1.5-pro-latest')
response = model.generate_content("Explain how IP address works in a few words")
print(response.text)
