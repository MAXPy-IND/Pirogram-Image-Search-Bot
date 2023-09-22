<p align="center">
<img style="width:100px; height:100px;" src="ImageSearchBot.PNG" alt="Pirogram-Image-Search-Bot Logo">
</p>

<h1 align="center">
<a href="https://github.com/MAXPy-IND/Pirogram-Image-Search-Bot">Pirogram Image Search Bot</a>
</h1>

<p align="center">
    <img src="https://img.shields.io/github/license/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/github/issues/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/MAXPy-IND/Pirogram-Image-Search-Bot?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

A Chat Bot written in python for search images..!!

### Credits

- Thanks to - [God..!](https://en.wikipedia.org/wiki/God)
- Thanks to - [Python..!](www.python.org)
- Thanks to - [IMDb..!](http://www.imdb.com/)
- Thanks to - [Requests..!](https://requests.readthedocs.io/0)
- Thanks to - [ME..!](https://github.com/MAXPy-IND)
- Thanks to - [Pirogram..!](https://tt.me/maxpy)

### Deployment

<details><summary>Tutorial Video</summary>
<p>
<br>
alt="Pirogram-IMDBot Logo">
</p>
</details>

- [x] Code

```
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
```

