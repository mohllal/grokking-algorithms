cache = {}

def get_data_from_server(url):
  print("Getting '{}' page data from server".format(url))
  return True

def get_page(url):
  if url in cache:
    print("Getting '{}' page data from cache".format(url))
    return cache[url]
  else:
    data = get_data_from_server(url)
    cache[url] = data 
    return data
  
if __name__ == "__main__":
  get_page("http://.../about")
  get_page("http://.../contact")
  get_page("http://.../about")
