class HttpRequest:
  def __init__(self):
    self.method = "GET"
    self.url = None
    self.headers = {}
    self.params = {}
    self.body = None
    
  def __str__(self):
    return (
      f"{self.method} {self.url}\n"
      f"Headers: {self.headers}\n"
      f"Params: {self.params}\n"
      f"Body: {self.body}"
    )

class HttpRequestBuilder:
  def __init__(self):
    self.request = HttpRequest()
  def set_url(self, url: str):
    self.request.url = url
    return self
  def set_method(self, method: str):
    self.request.method = method
    return self
  def add_header(self, key: str, value:str):
    self.request.headers[key] = value
    return self
  def add_param(self, key:str, value:str):
    self.request.params[key] = value
    return self
  def set_body(self, body:str):
    self.request.body = body
    return self
  def build(self):
    if not self.request.url:
      raise ValueError("URL must be set")
    return self.request
  
if __name__ == "__main__":
  # Builder design pattern example
  builder = HttpRequestBuilder()
  
  request = (
    builder
    .set_method("POST")
    .set_url("https://example.com/api")
    .add_header("Content-Type", "application/json")
    .add_param("query", "value")
    .set_body('{"key": "value"}')
    .build()
  )
  
  print(request)
  