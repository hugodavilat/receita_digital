SHELL=/bin/bash
install:
	sudo apt-get install python3
	sudo apt-get install python3-venv 
	python3 -m venv venv
	source venv/bin/activate; \
 	pip install -r requirements.txt
	
gendoc:
	openssl req -new -x509 -newkey rsa:2048 -keyout mock_doctor/privada.key -pubkey -out mock_doctor/privada.key -nodes -sha256
	
