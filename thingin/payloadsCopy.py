initial_data_json = [
    {
      "_iri": "|inserted_domain|androidIPCam",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/eupont.owl#Phone"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#description": "My android IP camera",
      "https://www.w3.org/2019/wot/td#name": "bureau-androidIPCam",
      "_outE": [
        {
          "_property": "https://www.w3.org/2019/wot/td#hasPropertyAffordance",
          "_iri": "|inserted_domain|androidIPCam.camera"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasActionAffordance",
          "_iri": "|inserted_domain|androidIPCam.torchOn"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasEventAffordance",
          "_iri": "|inserted_domain|androidIPCam.movementDetection"
        },
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#isContainedIn",
          "_iri": "|inserted_domain|bureau"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasPropertyAffordance",
          "_iri": "|inserted_domain|androidIPCam.luminance"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasActionAffordance",
          "_iri": "|inserted_domain|androidIPCam.torchOff"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/eupont.owl#Phone"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.movementDetection",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#MovementSensor"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "http://|local-ip|:8080/sensors.json?sense=motion_event",
      "https://www.w3.org/2019/wot/td#name": "movementDetection",
      "_class": "http://elite.polito.it/ontologies/dogont.owl#MovementSensor"
    },
    {
      "_iri": "|inserted_domain|bureau-Hue.state",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Sensor",
        "https://www.w3.org/2019/wot/td#PropertyAffordance"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/1",
      "https://www.w3.org/2019/wot/td#name": "state",
      "_class": "http://www.w3.org/ns/sosa/Sensor"
    },
    {
      "_iri": "|inserted_domain|salon-Hue",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Lamp"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#description": "Phillips Hue du salon",
      "https://www.w3.org/2019/wot/td#name": "salon-Hue",
      "_outE": [
        {
          "_property": "https://www.w3.org/2019/wot/td#hasPropertyAffordance",
          "_iri": "|inserted_domain|salon-Hue.state"
        },
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#isContainedIn",
          "_iri": "|inserted_domain|salon"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Lamp"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.luminance",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#LightSensor",
        "http://www.w3.org/ns/sosa/Sensor"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "http://|local-ip|:8080/sensors.json?sense=light",
      "https://www.w3.org/2019/wot/td#name": "luminance",
      "_class": "http://elite.polito.it/ontologies/dogont.owl#LightSensor"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.camera",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Sensor",
        "https://brickschema.org/schema/1.1/Brick#Camera"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "http://|local-ip|:8080/video",
      "https://www.w3.org/2019/wot/td#name": "camera",
      "_class": "http://www.w3.org/ns/sosa/Sensor"
    },
    {
      "_iri": "|inserted_domain|chambre-Hue",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Lamp"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#description": "Phillips Hue de la chambre",
      "https://www.w3.org/2019/wot/td#name": "chambre-Hue",
      "_outE": [
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#isContainedIn",
          "_iri": "|inserted_domain|chambre"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasPropertyAffordance",
          "_iri": "|inserted_domain|chambre-Hue.state"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Lamp"
    },
    {
      "_iri": "|inserted_domain|salon-Hue.state",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Sensor",
        "https://www.w3.org/2019/wot/td#PropertyAffordance"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/2",
      "https://www.w3.org/2019/wot/td#name": "state",
      "_class": "http://www.w3.org/ns/sosa/Sensor"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.torchOn",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Actuator"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "http://|local-ip|:8080/enabletorch",
      "https://www.w3.org/2019/wot/td#name": "enableTorch",
      "_class": "http://www.w3.org/ns/sosa/Actuator"
    },
    {
      "_iri": "|inserted_domain|chambre-Hue.state",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Sensor",
        "https://www.w3.org/2019/wot/td#PropertyAffordance"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/3",
      "https://www.w3.org/2019/wot/td#name": "state",
      "_class": "http://www.w3.org/ns/sosa/Sensor"
    },
    {
      "_iri": "|inserted_domain|chambre",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Room"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#name": "chambre",
      "_outE": [
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#connectsTo",
          "_iri": "|inserted_domain|salon"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Room"
    },
  {
    "_iri": "|inserted_domain|studio",
    "_domain": "|inserted_domain|",
    "_classes": [
      "http://elite.polito.it/ontologies/dogont.owl#Room"
    ],
    "_visibility": 0,
    "https://www.w3.org/2019/wot/td#name": "studio",
    "_outE": [
      {
        "_property": "http://ngsild.example.org/ngsild-ontology#connectsTo",
        "_iri": "|inserted_domain|salon"
      }
    ],
    "_class": "http://elite.polito.it/ontologies/dogont.owl#Room"
  },
    {
      "_iri": "|inserted_domain|bureau-Hue",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Lamp"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#description": "Phillips Hue du bureau",
      "https://www.w3.org/2019/wot/td#name": "bureau-Hue",
      "_outE": [
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#isContainedIn",
          "_iri": "|inserted_domain|bureau"
        },
        {
          "_property": "https://www.w3.org/2019/wot/td#hasPropertyAffordance",
          "_iri": "|inserted_domain|bureau-Hue.state"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Lamp"
    },
    {
      "_iri": "|inserted_domain|bureau",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Room"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#name": "bureau",
      "_outE": [
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#connectsTo",
          "_iri": "|inserted_domain|salon"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Room"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.torchOff",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://www.w3.org/ns/sosa/Actuator"
      ],
      "_visibility": 0,
      "http://www.w3.org/ns/tdo#href": "http://|local-ip|:8080/disableTorch",
      "https://www.w3.org/2019/wot/td#name": "torchOff",
      "_class": "http://www.w3.org/ns/sosa/Actuator"
    },
    {
      "_iri": "|inserted_domain|salon",
      "_domain": "|inserted_domain|",
      "_classes": [
        "http://elite.polito.it/ontologies/dogont.owl#Room"
      ],
      "_visibility": 0,
      "https://www.w3.org/2019/wot/td#name": "salon",
      "_outE": [
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#connectsTo",
          "_iri": "|inserted_domain|chambre"
        },
        {
          "_property": "http://ngsild.example.org/ngsild-ontology#connectsTo",
          "_iri": "|inserted_domain|bureau"
        }
      ],
      "_class": "http://elite.polito.it/ontologies/dogont.owl#Room"
    }
  ]




initialDataTTL= """
@prefix dogont: <http://elite.polito.it/ontologies/dogont.owl#> .
@prefix td: <https://www.w3.org/2019/wot/td#> .
@prefix brick: <https://brickschema.org/schema/1.1/Brick#> .
@prefix eupont: <http://elite.polito.it/ontologies/eupont.owl#> .
@prefix tdo: <http://www.w3.org/ns/tdo#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ngsi: <http://ngsild.example.org/ngsild-ontology#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

###############################
#Rooms
###############################

<|inserted_domain|salon> a dogont:Room ;
	ngsi:connectsTo <|inserted_domain|bureau> ;
	ngsi:connectsTo <|inserted_domain|chambre> ;
	td:name "salon"^^xsd:string .

<|inserted_domain|chambre> a dogont:Room ;
	ngsi:connectsTo <|inserted_domain|salon> ;
	td:name "chambre"^^xsd:string .

<|inserted_domain|bureau> a dogont:Room ;
	ngsi:connectsTo <|inserted_domain|salon> ;
	td:name "bureau"^^xsd:string .
	
###############################
#Lights (Phillips hue bulbs)
###############################

<|inserted_domain|salon-Hue> a dogont:Lamp ;
	td:hasPropertyAffordance <|inserted_domain|salon-Hue.state> ;
    ngsi:isContainedIn <|inserted_domain|salon> ;
    td:description "Phillips Hue du salon"^^xsd:string ;
    td:name "salon-Hue"^^xsd:string .

<|inserted_domain|bureau-Hue> a dogont:Lamp ;
	td:hasPropertyAffordance <|inserted_domain|bureau-Hue.state> ;
    ngsi:isContainedIn <|inserted_domain|bureau> ;
    td:description "Phillips Hue du bureau"^^xsd:string ;
    td:name "bureau-Hue"^^xsd:string .

<|inserted_domain|chambre-Hue> a dogont:Lamp ;
	td:hasPropertyAffordance <|inserted_domain|chambre-Hue.state> ;
    ngsi:isContainedIn <|inserted_domain|chambre> ;
    td:description "Phillips Hue de la chambre"^^xsd:string ;
    td:name "chambre-Hue"^^xsd:string .

#Lights affordances
<|inserted_domain|bureau-Hue.state> a td:PropertyAffordance,
    sosa:Sensor;
    td:name "state"^^xsd:string ;
    tdo:href "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/1"^^xsd:string .

	
<|inserted_domain|chambre-Hue.state> a td:PropertyAffordance,
    sosa:Sensor;
    td:name "state"^^xsd:string ;
    tdo:href "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/3"^^xsd:string .

	
<|inserted_domain|salon-Hue.state> a td:PropertyAffordance,
    sosa:Sensor;
    td:name "state"^^xsd:string ;
    tdo:href "https://192.168.1.47/api/75WMpeSrs1ogZ6kxD79ez-fseyPxaCNkt-r8YL1z/lights/2"^^xsd:string .

    


###############################
#Android IP camera
###############################

<|inserted_domain|androidIPCam> a eupont:Phone ;
    ngsi:isContainedIn <|inserted_domain|bureau> ;
    td:description "My android IP camera"^^xsd:string ;
    td:hasEventAffordance <|inserted_domain|androidIPCam.movementDetection> ;
	td:hasPropertyAffordance <|inserted_domain|androidIPCam.luminance> ;
	td:hasPropertyAffordance <|inserted_domain|androidIPCam.camera> ;
	td:hasActionAffordance <|inserted_domain|androidIPCam.torchOn> ;
	td:hasActionAffordance <|inserted_domain|androidIPCam.torchOff> ;
    td:name "bureau-androidIPCam"^^xsd:string .


<|inserted_domain|androidIPCam.movementDetection> a dogont:MovementSensor;
    td:name "movementDetection"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/sensors.json?sense=motion_event"^^xsd:string .

<|inserted_domain|androidIPCam.torchOn> a sosa:Actuator;
    td:name "enableTorch"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/enabletorch"^^xsd:string .

<|inserted_domain|androidIPCam.torchOff> a sosa:Actuator;
    td:name "torchOff"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/disableTorch"^^xsd:string .


<|inserted_domain|androidIPCam.luminance> a dogont:LightSensor, sosa:Sensor;
    td:name "luminance"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/sensors.json?sense=light"^^xsd:string .

<|inserted_domain|androidIPCam.camera> a brick:Camera, sosa:Sensor;
    td:name "camera"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/video"^^xsd:string ;
    tdo:href "http://|local-ip|:8080/video"^^xsd:string .
###############################
"""