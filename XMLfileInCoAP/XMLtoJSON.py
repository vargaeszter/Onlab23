import json
import xmltodict #pip install xmltodict
import xml_gen_no_NL

# source: https://www.geeksforgeeks.org/python-xml-to-json/ 2023-04-16 
 
# gen input
xml_gen_no_NL.XmlGen() 
# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
xml_file = open("XmlSource.xml", "r")
data_dict = xmltodict.parse(xml_file.read())
xml_file.close()
# generate the object using json.dumps()
# corresponding to json data
json_data = json.dumps(data_dict)
# Write the json data to output
# json file
json_file = open("JsonResult.json", "w")
json_file.write(json_data)
json_file.close()
