import boto3
import json
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

bedrock=boto3.client(service_name="bedrock-runtime")

# Variables for Bedrock API
modelId = 'anthropic.claude-3-sonnet-20240229-v1:0'
contentType = 'application/json'
accept = 'application/json'
prompt = "When was world war 2 fought?"

# Messages
messages = [
  {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": prompt
      }
    ]
  }
]

# Body
body = json.dumps({
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": messages
})

# Run Bedrock API
response = bedrock.invoke_model(
  modelId=modelId,
  contentType=contentType,
  accept=accept,
  body=body
)

# Print response
response_body = json.loads(response.get('body').read())
print(response_body['content'][0]['text'])