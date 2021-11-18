initial_data_json = [
    {
      "_iri": "|inserted_domain|androidIPCam",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Telephone"
      ],
      "_visibility": 0,
      "description": "My android IP camera",
      "nom": "insa-androidIPCam",
      "_outE": [
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|androidIPCam.camera"
        },
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|androidIPCam.torchOn"
        },
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|androidIPCam.movementDetection"
        },
        {
          "_label": "estDans",
          "_targetIRI": "|inserted_domain|salle_de_classe_insa"
        },
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|androidIPCam.luminance"
        },
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|androidIPCam.torchOff"
        }
      ]
    },
    {
      "_iri": "|inserted_domain|androidIPCam.movementDetection",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Capteur",
        "Capteur_de_mouvement"
      ],
      "_visibility": 0,
      "lien-http": "http://|local-ip|:8080/sensors.json?sense=motion_event",
      "nom": "movementDetection"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.luminance",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Capteur",
        "Capteur_de_luminosite"
      ],
      "_visibility": 0,
      "lien-http": "http://|local-ip|:8080/sensors.json?sense=light",
      "nom": "luminance"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.camera",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Capteur",
        "Camera"
      ],
      "_visibility": 0,
      "lien-http": "http://|local-ip|:8080/video",
      "nom": "camera",
      "_outE": [
        {
          "_label": "observe",
          "_targetIRI": "|inserted_domain|ecran.display"
        }
      ]
    },
    {
      "_iri": "|inserted_domain|ecran",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Moniteur"
      ],
      "_visibility": 0,
      "nom": "ecranPC",
      "_outE": [
        {
          "_label": "estDans",
          "_targetIRI": "|inserted_domain|salle_de_classe_insa"
        },
        {
          "_label": "dispose_de",
          "_targetIRI": "|inserted_domain|ecran.display"
        }
      ]
    },
    {
      "_iri": "|inserted_domain|ecran.display",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Affichage"
      ],
      "_visibility": 0,
      "nom": "ecranDisplay",
      "_outE": [
        {
          "_label": "observe",
          "_targetIRI": "|inserted_domain|androidIPCam.camera"
        }
      ]
    },
    {
      "_iri": "|inserted_domain|androidIPCam.torchOn",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Actuateur"
      ],
      "_visibility": 0,
      "lien-http": "http://|local-ip|:8080/enabletorch",
      "nom": "enableTorch"
    },
    {
      "_iri": "|inserted_domain|androidIPCam.torchOff",
      "_domain": "|inserted_domain|",
      "_labels": [
        "Actuateur"
      ],
      "_visibility": 0,
      "lien-http": "http://|local-ip|:8080/disableTorch",
      "nom": "torchOff"
    }
]


