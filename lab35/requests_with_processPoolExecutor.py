import requests
import time
import threading
import concurrent.futures

def downlload_image(url):
    file_name = url.split('/')[4]+".jpg"

    # get image bytes
    print(f"Start downloading {url}")
    response = requests.get(url)

    # write image to file
    with open(file_name, 'wb') as fh:
        fh.write(response.content)

    print(f"File saved to {file_name}")

start = time.perf_counter()
urls = [
    "https://unsplash.com/photos/CTflmHHVrBM/download?force=true",
    "https://unsplash.com/photos/pWV8HjvHzk8/download?force=true",
    "https://unsplash.com/photos/1jn_3WBp60I/download?force=true",
    "https://unsplash.com/photos/8E5HawfqCMM/download?force=true",
    "https://unsplash.com/photos/yTOkMc2q01o/download?force=true"
]

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(downlload_image, urls)


end = time.perf_counter()
print(f"Downloaded in {round(end-start, 2)} seconds")

# File saved to CTflmHHVrBM.jpg
# File saved to yTOkMc2q01o.jpg
# File saved to 8E5HawfqCMM.jpg
# File saved to 1jn_3WBp60I.jpg
# File saved to pWV8HjvHzk8.jpg
# Downloaded in 11.45 seconds