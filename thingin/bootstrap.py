import uuid
import json
from thingin.payloads import *
from thingin.thingin_requests import *
import sys

def append_my_uuid(my_uuid, data):
    for node in data:
        node["_iri"] += "-" + str(my_uuid)
        if "_outE" in node:
            for edge in node["_outE"]:
                if not str(edge["_targetIRI"]).__contains__("salle_de_classe_insa") and not str(edge["_targetIRI"]).__contains__("couloir"):
                    edge["_targetIRI"] += "-" + str(my_uuid)
    return data

def set_domain(domain_to_insert, data):
    inserted_domain_string = "|inserted_domain|"
    for node in data:
        node["_iri"] = node["_iri"].replace(inserted_domain_string, domain_to_insert)
        node["_domain"] = node["_domain"].replace(inserted_domain_string, domain_to_insert)
        if "_outE" in node:
            for edge in node["_outE"]:
                edge["_targetIRI"] = edge["_targetIRI"].replace(inserted_domain_string, domain_to_insert)
    return data

def set_ip(ip_to_insert, data):
    inserted_ip_string = "|local-ip|"
    for node in data:
        if "lien-http" in node:
            node["lien-http"] = node["lien-http"].replace(inserted_ip_string, ip_to_insert)
    return data



##BOOSTRAP SEQUENCE##

print("###########################")
print("Program arguments : ")
for arg in sys.argv:
    print(arg)

token = sys.argv[1]
domain_to_insert = sys.argv[2]
name = sys.argv[3]
ip = sys.argv[4]
print("###########################")


my_uuid = uuid.uuid3(namespace=uuid.NAMESPACE_DNS, name=name)
my_data = set_domain(domain_to_insert, initial_data_json)
my_data = set_ip(ip, my_data)
my_data = append_my_uuid(my_uuid, my_data)

print("######### Data ##########")
print(json.dumps(my_data))
print("###########################")

print("######### Access token ##########")
print(token)
print("###########################")


print("Posting initial data to thingin")
bootstrap_request = post_initial_data(my_data, token)


print("Result of upload : "+bootstrap_request.text)
if bootstrap_request.text != "\"Probably duplicate\"\n":
    result_data = bootstrap_request.json()
    print("###########################")
    print("Saving uuids for future updates")
    f1 = open('boostrap_result.json', 'w')
    f1.writelines(json.dumps(result_data))
    print("Saved to boostrap_result.json")
    print("###########################")
else:
    print("Bootstrap already done, erase following data if you want to reset")
    f1 = open('boostrap_result.json', 'r')
    my_data_on_thingin = json.dumps(json.load(f1))
    print(my_data_on_thingin)