import requests
from io import BytesIO
from PIL import Image
import os

UNSPLASH_API_KEY = 'd_jUuJJq5QhpkZAfyp-JSJJkC4OuAC3pJq-0z5Vf35I'

def search_images(query, num_results=5):
    base_url = 'https://api.unsplash.com/search/photos'

    headers = {
        'Authorization': f'Client-ID {UNSPLASH_API_KEY}'
    }

    params = {
        'query': query,
        'per_page': num_results
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data['results']
        return results
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return []

def display_images(images):
    for idx, image in enumerate(images):
        print(f"Image {idx + 1}: {image['urls']['regular']}")
        response = requests.get(image['urls']['regular'])
        img_data = BytesIO(response.content)
        img = Image.open(img_data)
        img.show()

if __name__ == "__main__":
    while True:
        search_query = input("Enter your image search query (or 'exit' to quit): ")

        if search_query.lower() == 'exit':
            break

        num_results = int(input("Enter the number of results to display: "))
        images = search_images(search_query, num_results)

        if images:
            display_images(images)
        else:
            print("No images found for the given query.")
