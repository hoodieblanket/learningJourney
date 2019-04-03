#Classes

Classes are a template of behaviours and structure that you use for things that behave the same way or share meaning.

This template is used to make it easier to manage similar objects or classes of objects. For example: If you had \
a `dog` class then you would share similarities between all dogs such as they all have a `name, colour and breed` and\
they all have the same behaviour `barking, running and wagging tail`.

the `__init__` method is a constructor often referred to as a *magic method*. This method is called when the instance of\
the class is created. It's own frame is created and then the magic method initialises the template setup.

So __init__ is used by programmers to initialise values when a given instance or frame is created.

**For Example**
```python
class Article(object):
    def __init__(self, title):
        self.title = title
        self.published = False
    def __unicode__(self):
        return self.title
    def publish(self):
        self.published = True
        
nyt_article = Article("Christie Faces Scandal on Traffic Jam Aides Ordered")
```

*Self* refers to the instance or frame of a given class which in this case is a Article
`nyt_article.title` This would return the title that was set for the self.title = "Christie faces scandal..."\
`nyt_article.published` This would return the value of self.published which is currently in the instance set to False.\
`unicode(nyt_article)` This would use the unicode method, which in this instance would *return self.title* "christie..."\
`publish(nyt_article)` This would set self.published to True and as a result the instance would now be True for Published\

