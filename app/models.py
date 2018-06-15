class News_Sources:
    """
    clas to define the objects in the News_Sources class
    """
    def __init__(self,id,name,description,category,url,country,language):
        '''
        function to initialize the behaviours of the class
        '''

        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.url=url
        self.country=country
        self.language=language

class News_Article:
    """class to define the objects in the News_Article class"""
    def __init__(self,id,title,author,url,image,description,date):
        self.id=id
        self.title=title
        self.author=author
        self.url=url
        self.image=image
        self.description=description
        self.date=date
