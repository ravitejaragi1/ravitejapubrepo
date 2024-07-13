import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help = "The prompt to send to chatgpt")
parser.add_argument("output_file_name", help = "to save the generated code")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key_file = open("chatgptkey.txt",'r')
api_key = api_key_file.read()

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key 
}

request_data = { 
    "model": "text-davinci-003",
    "prompt": f"write python script to {args.prompt}",
    "max_tokens": 1000,
    "temperature": 0.5 

}

response = requests.post(api_endpoint, headers=headers, json=request_data)

if response.status_code == 200:
#   print(response.json())

    response_text=response.json()["choices"][0]["text"]

    with open(f"{args.output_file_name}.py","w") as file:
        file.write(response_text)
   

else :
    print(f"request failed: {str(response.status_code)}")
    print(response.text)




