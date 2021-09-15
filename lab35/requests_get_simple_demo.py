import requests
import time

start = time.perf_counter()
url = "https://unsplash.com/photos/CTflmHHVrBM/download?force=true"
file_name = url.split('/')[4]+".jpg"

# get image bytes
print(f"Start downloading {url}")
response = requests.get(url)

# write image to file
with open(file_name, 'wb') as fh:
  fh.write(response.content)
  print(f"File saved to {file_name}")

end = time.perf_counter()
print(f"Downloaded in {round(end-start, 2)} seconds")