import requests as req
import time
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "akt99"
TOKEN = "Z!X@C#V$B%N^m7"
GRAPH_ID="graphtest1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
#response=req.post(url=pixela_endpoint,json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# print("Starting the request to create a graph...")
#
# try:
#     start_time = time.time()
#     response = req.post(url=graph_endpoint, json=graph_config, headers=headers, timeout=10)
#     elapsed_time = time.time() - start_time
#     print(f"Request completed in {elapsed_time:.2f} seconds")
#
#     # Print response status code and text for debugging
#     print("Response status code:", response.status_code)
#     print("Response text:", response.text)
#
#     # Check if graph creation was successful
#     if response.status_code == 200:
#         print("Graph created successfully.")
#     else:
#         print("Failed to create graph.")
# except req.exceptions.Timeout:
#     print("The request timed out. Please try again later.")
# except req.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")
try:
    print("Creating graph...")
    response = req.post(url=graph_endpoint, json=graph_config, headers=headers, timeout=10)
    print("Graph creation response:", response.text)
except req.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except req.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Endpoint and data for creating a pixel in the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": "20240531",
    "quantity": input("How many kilometres did you cycle today? "),
}

# Add a pixel to the graph
try:
    print("Adding pixel...")
    response = req.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data, timeout=10)
    print("Pixel creation response:", response.text)
except req.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except req.exceptions.RequestException as e:
    print(f"An error occurred: {e}")