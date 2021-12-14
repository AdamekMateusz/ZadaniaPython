from xml.dom import minidom
xmldoc = minidom.parse('user.xml')

tags = xmldoc.getElementsByTagName("user")

for item in tags:
    #print(item.attributes["firstname"].value)
    if item.attributes["id"].value == '102':
        item.attributes["id"].value = item.attributes["id"].value.replace(
            "102", "103")

with open("user_update.xml", "a+") as f:
    xmldoc.writexml(f)