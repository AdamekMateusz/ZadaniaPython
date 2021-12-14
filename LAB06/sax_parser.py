import xml.sax

from xml.sax.saxutils import XMLFilterBase, XMLGenerator
import sys

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ''
        self.firstname = ''
        self.lastname = ''
    
    def startElement(self, tag, attributes):
        self.CurrentData  = tag
        if tag == 'user':
            print('--USER--')
            id = attributes['id']
            print('id:', id)
            
            # xmlwriter.startElement(name=tag, attrs={})

            
    
    def endElement(self, tag):
        if self.CurrentData == 'firstname':
            print('firstname: ', self.firstname)
            # xmlwriter.endElement(name=tag)
        elif self.CurrentData == 'lastname':
            print('lastname: ', self.lastname)
            # xmlwriter.endElement(name=user)

        self.CurrentData = ''
        
    
    def characters(self, content):
        if self.CurrentData =='firstname':
            self.firstname = content
        elif self.CurrentData == 'lastname':
            self.lastname = content

if (__name__=='__main__'):

    # xmlwriter.startElement(name=self.name, attrs={})
    # xmlwriter.endElement(name=self.name)

    output = sys.stdout
    encoding = 'utf-8'

    # xmlwriter = XMLGenerator(output, encoding, short_empty_elements=True)
    # xmlwriter.startDocument()

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)

    Handler = XMLHandler()
    parser.setContentHandler(Handler)

    parser.parse('user.xml')

