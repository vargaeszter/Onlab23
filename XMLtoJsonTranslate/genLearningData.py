import json
import xmltodict #pip install xmltodict
import XMLgen
NumTrain = 10000
NumVal = 1000
NumTest = 200

# 0.lépés modif
# ne legyen többszintű beágyazás
# 10 kiválasztott tag véletlenszerűen összekeverve
# 100 sample

xml_file = open("src_xml_train.xml", "w")
json_file = open("tg_json_train.json", "w")

for m in range(NumTrain):
    xmlString = XMLgen.XmlGen() 
    xml_file.write(xmlString)
    data_dict = xmltodict.parse(xmlString)
    json_data = json.dumps(data_dict)
    json_file.write(json_data)
    if(m != NumTrain - 1):
        xml_file.write('\n')
        json_file.write('\n')

xml_file.close()
json_file.close()

xml_file = open("src_xml_val.xml", "w")
json_file = open("tg_json_val.json", "w")

for m in range(NumVal):
    xmlString = XMLgen.XmlGen() 
    xml_file.write(xmlString)
    data_dict = xmltodict.parse(xmlString)
    json_data = json.dumps(data_dict)
    json_file.write(json_data)
    if(m != NumVal - 1):
        xml_file.write('\n')
        json_file.write('\n')

xml_file.close()
json_file.close()

xml_file = open("src_xml_test.xml", "w")
json_file = open("tg_json_test.json", "w")

for m in range(NumTest):
    xmlString = XMLgen.XmlGen() 
    xml_file.write(xmlString)
    data_dict = xmltodict.parse(xmlString)
    json_data = json.dumps(data_dict)
    json_file.write(json_data)
    if(m != NumTest - 1):
        xml_file.write('\n')
        json_file.write('\n')

xml_file.close()
json_file.close()