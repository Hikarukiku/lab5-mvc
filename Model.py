import xml.etree.ElementTree as ET

class Animal(object):
    def __init__(self, type_a = None, name_a = None):
        self.type_a = type_a
        self.name_a = name_a

    def name(self):
        return(self.type_a + " " + self.name_a)

    @classmethod     
    def getAll(self):
        db = ET.parse("db.xml")
        root = db.getroot()
        result = []
        for child in root:
            person = Animal(child.find("type").text, child.find("Name").text)
            result.append(person)
        return result


