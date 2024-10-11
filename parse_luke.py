import xml.etree.ElementTree as ET
#TASK: look up the documentation for this

# Load and parse XML file
tree = ET.parse('luke.txt')

root = tree.getroot()

output = ""
for chapter in root.findall('chapter'):
    chapter_number = chapter.get('display')
    output += f"Ch.{chapter_number}"
    for verse in chapter.findall('.//verse'):
        verse_number = verse.get('display-number', 'N/A')
        verse_text = ''.join(verse.itertext()).strip()
        #print(f"Verse {verse_number}: {verse_text}")
        output += verse_text
    #print()

if output:
    with open("fluke.txt", "w", encoding="utf-8") as file:
        file.write(output)
    print("Final Luke text successfully added to fluke.txt")
else:
    print("output was empty, some error dude")
