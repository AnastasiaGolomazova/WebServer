from object.abstractobject import AbstractObject

class WebPages(AbstractObject):
 
    def __init__(self, id, name, text):
        AbstractObject.__init__(self, id, name)
        self.Text = text


    def toJsonName(self):
        return f'{{"id" : {self.Id}, "name" : "{self.Name}"}}'

    def toJsonText(self):
        return f'{{"id" : {self.Id}, "text" : "{self.Text}"}}'