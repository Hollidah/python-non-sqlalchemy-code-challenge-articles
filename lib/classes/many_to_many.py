class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)      # To add new articles to the list of articles.


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else: 
            raise ValueError ("Title must be a string between 5 to 50 characters.")


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author (self, value):
        if isinstance (value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of Author")

    
    @property
    def magazine (self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance (value, Magazine):
            self._magazine = value
        else:
            raise ValueError ("Magazine must be an instance of Magazine")

        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after instantiation")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):            # Returns the list of articles written by the author
        return [article for article in Article.all if article.author == self]

    def magazines(self):            # Returns a unique list of magazines the author has contributed
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):        # Creates a new article and adds it to the author's article list
        return Article(self, magazine, title)

    def topic_areas(self):              # Returns a list of magazine categories the author has contributed to
        if self.articles():
            return list(set(magazine.category for magazine in self.magazines()))
        return None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category (self):
        return self._category

    @category.setter
    def category (self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):         # Artciles published by the magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):     # List of authors who have contributed to the magazine
        return list(set(article.author for article in self.articles()))

    def article_titles(self):   # List of article titles published by the magazine
        if self.articles():
            return [article.title for article in self.articles()]
        return None

    def contributing_authors(self):     # List of authors who have written more that 2 articles for the magazine
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
            contributors = [author for author, count in author_counts.items() if count > 2]
        if not contributors:
            return None
        return contributors
            