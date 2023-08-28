# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import json
from prompts import anki, anki_card_comparison

openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("AZURE_OPENAI_KEY_1")
ENGINE_NAME = "EricChatGPT"
CURRENT_PROMPT = 'AtreidesAI'

with open('./prompts/misc.json', 'r', encoding="utf8") as f:
    system_message = json.loads(f.read())[CURRENT_PROMPT]

current_message = [{
    "role": "system",
    "content": ""# anki_card_comparison.CardEditor
}] + [{
    "role": "user",
    "content": "wpw syndrome"}]

print('prompting...')
response = openai.ChatCompletion.create(
    engine=ENGINE_NAME,  # engine = "deployment_name".
    messages=current_message
)
response_message = [{"role": "assistant", "content": response['choices'][0]['message']['content']}]
print(response_message[0]['content'])
