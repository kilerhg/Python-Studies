# we have imported the requests module
import requests
import json
# defined a URL variable that we will be
# using to send GET or POST requests to the API
url = "http://0.0.0.0:8000/graphql"
 
body = """
{
  books(title: "The Great Gatsby") {
    title
    author
  }
}
"""
 
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
    print("response : ", json.loads(response.content))