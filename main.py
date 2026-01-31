# Joshua CS 152 Self Practice
# Trying to work with JSON to have cleaner code
import json

with open("map.json","r") as f:
    data = json.load(f)

print(data) 
