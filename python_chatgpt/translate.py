

#Importing libraries
import requests
from bs4 import BeautifulSoup
import googletrans

#Defining the target URL
url = "https://www.stackoverflow.com"

#Making a request to the URL
req = requests.get(url)

#Getting the HTML content
html = req.content

#Parsing the HTML content
soup = BeautifulSoup(html, 'html.parser')

#Finding all the headers
headers = soup.find_all(['h1','h2','h3','h4'])
#Creating a list of headers
headers_list = [header.text for header in headers]

#Creating a translator object
translator = googletrans.Translator()

#Creating a list of translated headers
translated_headers = [translator.translate(header, dest='te').text for header in headers_list]

print(translated_headers)
#Writing the list of translated headers to an HTML file
with open('headers.html', 'w') as f:
    f.write('<html>\n<body>\n')
    for header in translated_headers:
        f.write(f'<h1>{header}</h1>\n')
    f.write('</body>\n</html>')