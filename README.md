
#EN
# Initiation ThingIn via PyDroidIpcam

Forked from https://github.com/home-assistant-libs/pydroid-ipcam 

Content:

Requirements: python3 + android device connected to the same local network
Optional : raspberry + sensehat, other objects

- install "IP Webcam" apk from google play store on your android device
- launch the app. Tick "Activate sensors" in the application, and accept security authorizations. If wanted you can set a password (camera feed will remain local)
- download the above repository containing data to be completed and python scripts that will emit data from the device to thingin (i.e. torch state, lgiht sensor value...) 
- set up a functional python3 environment with the repository's required packages (see requirements.txt), where $PROJECT_FOLDER is the path to pydroid-ipcam folder on your machine: 
	- ``` export PYTHONPATH=PYTHONPATH:$PROJECT_FOLDER/ , ou commande équivalente windows ```
	- ``` cd $PROJECT_FOLDER/thingin ```
	- All python scripts used in this exercice can be launched from an IDE or from command line, with the following arguments (respect argument order): 
	``` "$THING_TOKEN" "$THINGIN_DOMAIN" "$FIRSTNAME_NAME" "$IPCAM_IP" "$IP_CAM_USER" "$IP_CAM_PWD" "$TORCH_ON_OFF" ``` 

		$THING_TOKEN: your thingin access token at https://tech2.thinginthefuture.com (see credentials given below)
		$THINGIN_DOMAIN: thingin domain to be used to store your data. The domain to be used is already created: http://www.example.com/insa/
		$FIRSTNAME_NAME: used to generate a unique key if multiple users want to use the same account in this exercice (can be any another passphrase). 
		$IPCAM_IP": the IP address of your android device on your local network
		$IP_CAM_USER: Username set in IP Webcam application (let empty string "" if no password)
		$IP_CAM_PWD: Password set in IP Webcam application (let empty string "" if no password)
		$TORCH_ON_OFF: used to test your environment. Puts the android deveice torch status ON/OFF
		Exemple : 
		``` python3 bootstrap.py "Bearer 12345" "http://www.example.com/insa/" "thomas_hassan" "192.168.1.18" "Test" "Test" "ON" ```
		
- Main exercice:
	- Test your environment and visualize initial data: 
		- Find your android device's IP address
		- Connect to https://tech2.thinginthefuture.com. The guest credentials for the exercice are: 
			Email : thingin-demo@orange.com
			Password : thingin-demo147
		- Get your user token: Develop tab -> Get My Thing in token -> Copy to Clipboard
		- Start the android IP Webcam server on the device. If necessary change the login/password. 
		- Execute the script torch_test.py by using the arguments used during installation. Example : ``` python3 torch_test.py  "Bearer 12345" "http://www.example.com/insa/" "thomas_hassan" "192.168.1.18" "Test" "Test" "ON" ```
	- (Re)Connect to ThingIn's website with your credentials 
	- Familiarize yourself with thingin's visualization tools (graph2D / graph3D / Map / Raw): you can test ThingIn portal functionnalities with other domains first (Explore Tab -> Explore ThingIn database -> Select a request -> Get results)
	- Optional Developers: take a look at ThingIn's API l'api (swagger). We will reach this API through code in this exercice.  
	- Create your environment in ThingIn:
		- Optional : jfirst take a look at the base data we are going to inject, in the file payloads.py
		- Execute the script bootstrap.py (with arguments)
		- The file boostrap_result.json should be created in the current path and contain ThingIn's injection response, with the following syntax (if the server is busy, an error may occur, retry the command): 
			``` [{"uuid": "b02531f3-8c48-480b-8259-aa256b7dbff3", "iri": "http://www.example.com/insa/androidIPCam-a82aeb9d-31a5-3f52-8714-4c47ae4e74fd", "isIn": []}, {"uuid":  .... ] ```
			the response is the list of created nodes in ThingIn, where uuid is the internal identifier for the node, and iri is its global identifier, postfixed by a hash based on the $FIRSTNAME_NAME argument.
	- Request the resulting data in thingin: 
		Explore Tab-> Explore ThingIn Database -> Select the request "Test your own domain" -> tick advanced mode -> replace the query with the following:
		```
		{	
		  "query": {
			"$domain": "http://thingin.orange.com/users/thingin-demo/"
		  },
		  "view": {}
		}
		```
	- The above request gets all avatars in the domain ```http://thingin.orange.com/users/thingin-demo/```. Since this domain is shared with other other users of this account,we are going to make a request to select only the avatars you just created using graph traversal in Thingin:
		- Still using the tab ```Explore the Thing in database```, change the request type using the drop down menu, from ```POST``` to ```GET```
		- Get the internal UUID of the android device, which is stored in the bootstrap_result.json file: it is the first piece of data in the file, its iri should be of the form  ``` http://www.example.com/insa/androidIPCam-$hash ```, copy and paste the ```UUID``` field
		- Fill in the following request url on the right of the drop POST/GET drop down menu: /avatars/$uuid?Read-Mode=depth&Read-Depth=10, by replacing ```$uuid``` with the uuid found in the previous step
		- Click the Get results button. The result of the request is your data, which should contain 9 nodes and 10 edges
	- Look at your data using any of the view (2D, raw...), and search for the IP webcam HTTP endpoints: they are stored as a property of the nodes which refer to the sensors. If using a graph view, click on a node to show its properties on the right panel
	- We are going to launch a script that will periodically update our data in thingin: execute  ```main.py``` in the repository root folder. The script uses the API of IP webcam to get data from sensors, and the API of ThingIn to update the nodes periodically (every 5 sec)
	- Look at your data again in ThingIn using the previous request, and verify the updates on your nodes.
	- The data that we sent with bootstrap.py are describedi n the file payloads.py. We are going to modify/complete payloads.py to add new nodes/edges and improve the data sent periodically.
		- Create a new variable and construct a new payload for a new set of nodes/edges in payloads.py. We are going to add the torchlight of the android device, and you can also add some nodes for your rooms: create a node for each room, and an edge for each connection (take from example the previous data in payloads.py) 
			- Edit bootstrap.py to use the new variable with new nodes
		- Complete missing data for the torchlight node, by editing thingin_requests.py and main.py: 
			- Define a new function ```put_torch_status_thingin``` in thinin_requests.py. Use as examples the exiting functions for motion and light
			- Use the function definined above in main.py, by calling it in ```update_data(cam)```
	- Once the new payload is created and the scripts are edited, launch main.py again. Go back to ThingIn portal to see the updates
	- Optional: in the same manner as you added nodes for the torchlight and rooms, create new nodes for your other devices (lights...)
		- To create the nodes for your devices, you need to declare them with an ontology class. To find this class you can use ThingIn ontology explorer: Explore Tab -> ontology lookup service -> search classes in OLS


#FR
# Initiation ThingIn via PyDroidIpcam

Forked from https://github.com/home-assistant-libs/pydroid-ipcam 

Contenu du TP:

Requis : un PC avec python3 installé + Device android connectés au même réseau local et à internet
Optionel : raspberry + sensehat, autre objets

- installer l'apk "IP Webcam" sur votre device android
- activer les capteurs dans l'appli, accepter les demandes d'autorisations. Définir un mot de passe si souhaité
- télécharger le dépôt ci-dessus comprenant des données préconstruites et des scripts python d'update des données d'ipcam vers thingin (état de la torche, valeur du capteur de lumière...) 
- mettre en place un environnement python fonctionnel avec les dépendances du dépôt, où $PROJECT_FOLDER est le chemin d'accès au dossier pydroid-ipcam : 
	- ``` export PYTHONPATH=PYTHONPATH:$PROJECT_FOLDER/ , ou commande équivalente windows ```
	- ``` cd $PROJECT_FOLDER/thingin ```
	- Tous les scripts python3 utilisés dans le TP ci-dessous peuvent être lancés depuis un IDE ou un interpréteur avec les arguments suivants (ordre des arguments et syntaxe à respecter): 
	``` "$THING_TOKEN" "$THINGIN_DOMAIN" "$PRENOM_NOM" "$IPCAM_IP" "$IP_CAM_USER" "$IP_CAM_PWD" "$TORCH_ON_OFF" ``` 

		$THING_TOKEN : votre token à récupérer sur https://tech2.thinginthefuture.com (voir ci-après dans le descriptif du TP)
		$THINGIN_DOMAIN : domaine à utiliser où vos données seront enregistrées dans thingin (1 domaine commun à tous les étudiants). Le domaine à utiliser est : http://www.example.com/insa/
		$PRENOM_NOM : utilisé pour générer une clé unique (peut être une autre passphrase, tant qu'elle n'est pas partagée par d'autres étudiants). 
		$IPCAM_IP" : l'ip locale de votre device android où est installé android ipcam
		$IP_CAM_USER : Nom d'utilisateur du serveur android IP Webcam (à définir dans l’application)
		$IP_CAM_PWD : Password du serveur android IP Webcam (à définir dans l’application)
		$TORCH_ON_OFF : ON ou OFF (pour allumer / éteindre la torche du device, utilisé uniquement pour tester l’installation)
		Exemple : 
		``` python3 bootstrap.py "Bearer 12345" "http://www.example.com/insa/" "thomas_hassan" "192.168.1.18" "Test" "Test" "ON" ```
		
- coeur du TP :
	- Test d'installation et visualisation des données initiales : 
		- Récupérer l'ip de votre device android 
		- Se connecter à https://tech2.thinginthefuture.com. Les credentials à utiliser sont : 
			Email : thingin-demo@orange.com
			Password : thingin-demo147
		- Récupérer son token : onglet Develop -> Get My Thing in token -> Copy to Clipboard
		- Lancer le serveur android ipcam sur votre device. Si nécessaire changer la résolution vidéo et le login/mot de passe. Si pas de login mot de passe dans l'application, laissez les arguments vides ("") en lançant les scripts
		- Tester l'environnement : exécuter le script torch_test.py en utilisant les arguments correspondants à votre installation. Exemple : ``` python3 torch_test.py  "Bearer 12345" "http://www.example.com/insa/" "thomas_hassan" "192.168.1.18" "Test" "Test" "ON" ```
	- se (re)connecter à la plateforme ThingIn avec les credentials fournis pour vérifier vos données uploadées (et celles des autres étudiants)
	- Se familiariser avec les vues du portail (graph2D / graph3D / Map / Raw) 
	- Optionel : regarder l'api (swagger) de thingin. On accèdera ensuite à cette api à travers le code utilisé pour accéder à vos données créées dans thingin  
	- créer son environnement local dans thingin:
		- Optionnel : jeter un œil aux données qui vont être injectées, cf. fichier payloads.py
		- Exécuter le script bootstrap.py (avec arguments, cf. ci-dessus)
		- le fichier boostrap_result.json devrait être créé dans le répertoire courant et contenir la réponse de l’API thingin à la création, de la forme : 
			``` [{"uuid": "b02531f3-8c48-480b-8259-aa256b7dbff3", "iri": "http://www.example.com/insa/androidIPCam-a82aeb9d-31a5-3f52-8714-4c47ae4e74fd", "isIn": []}, {"uuid":  .... ] ```
			où uuid est l'identifiant interne du noeud, et iri son identifiant global, suffixé par votre hash pour ce TP.
	- Requêter son environnement thingin: 
		Onglet Explore -> Explore ThingIn Database -> Sélectionner la requête "Test your own domain" dans le menu déroulant -> cocher advanced mode -> entrer la requête suivante (requête de type POST)
		```
		{	
		  "query": {
			"$domain": "http://thingin.orange.com/users/thingin-demo/"
		  },
		  "view": {}
		}
		```
	- La requête ci-dessus renvoie les avatars communs à tous les étudiants. Pour sélectionner uniquement vos avatars, nous allons exécuter une requête en profondeur à partir d'un de vos noeuds (Spécificité due au TP à distance):
		- Toujours dans la page Explore the Thing in database, changer le type de requête : menu déroulant POST->GET
		- Récupérer l'identifiant interne du noeud correspondant au téléphone, dont l'iri est de la forme ``` http://www.example.com/insa/androidIPCam-$hash ```, stocké dans le fichier bootstrap_result.json. Il devrait s'agir du premier noeud de la liste. Bien prendre l'uuid, pas votre hash qui suit l'iri.
		- Entrer l'url de requête GET suivante à droite du menu déroulant : /avatars/$uuid?Read-Mode=depth&Read-Depth=10, en remplaçant $uuid par l'uuid récupéré précédemment
		- Le résultat de cette requête devrait contenir uniquement votre environnement, composé de 9 noeuds et 10 edges
	- Retrouver les endpoints de l’API android ipcam dans les propriétés des nœuds correspondants aux différents capteurs à travers l’interface ThingIn. Pour afficher les propriétés d'un noeud il suffit de cliquer dessus
	- Lancer le script de mise à jour des données dans thingin, ```main.py```, qui accède à l'API du device, récupère les données et accède à l'API de thingin pour mettre à jour les noeuds précédemment créés de façon continue (environ toutes les 5 secondes)
	- Vérifier la mise à jour des données dans thingin via la visualisation
	- Les données qui ont été uploadées dans thingin par le bootstrapper sont décrites dans le fichier payloads.py. Nous allons créer de nouvelles données pour les compléter.
		- Construire un nouveau payload pour les noeuds (pièces et torche du device) ainsi créés, les assigner à une nouvelle variable dans payloads.py
		- Compléter ces données avec d'autres objets de l'environnement physiques (pièces et relations entre elles), en prenant en exemple les données existantes. 
			- Modifier bootstrap.py pour utiliser la variable contenant les nouveaux noeuds
		- Compléter les données manquantes pour le device IPcam (noeud décrivant le status actuel de la torche). Pour accéder à l'état de la torche et faire sa mise jour dans thingin, les fichiers thingin_requests.py et main.py doivent être édités : 
			- Définir une nouvelle fonction put_torch_status_thingin dans thinin_requests.py, en prenant exemple sur les fonctions existantes (motion et light)
			- Utiliser la fonction précédemment créée dans main.py, dans la fonction update_data(cam)
	- Vérifier de nouveau la mise à jour des données dans thingin via la visualisation (relancer le script main.py)
	- Optionnel : de la même façon que pour les nouveaux noeuds pour les pièces et la torche, déclarer des noeuds pour vos autres devices. 
		- Les classes à utiliser pour déclarer vos objets peuvent être recherchés dans thingin : Onglet explore -> ontology lookup service -> search classes in OLS
