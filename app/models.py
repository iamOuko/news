
class News():
    def __init__(self, id,name,description,country,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.country = country
        self.url = url
        self.category = category

      

class Article():
    def __init__(self, author, title, description, url, urlToImage, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.content = content