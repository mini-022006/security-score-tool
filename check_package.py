import json

package = input("Enter package name: ")

with open("vulnerability_db.json") as f:
    data = json.load(f)

if package in data:
    print("Package:", package)
    print("Security Score:", data[package]["score"])
    print("Risk Level:", data[package]["risk"])
else:
    print("No data found. Package assumed safe.")