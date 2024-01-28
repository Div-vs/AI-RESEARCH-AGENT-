import requests
import json

print(
    requests.post(
        "http://127.0.0.1:8000",
        json={
            "query": "what is meta ?"
        }
    ).json()
)