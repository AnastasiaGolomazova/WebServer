from object.abstractobject import AbstractObject

class WebPages(AbstractObject):
 
    def __init__(self, id, text):
        AbstractObject.__init__(self, id, '')
        self.Text = text