run-dev:
	@echo
	@echo '[+] Executing flask with Development settings...'
	@echo
	FLASK_APP=flaskr FLASK_ENV=development flask run

run-prod: init-db
	@echo
	@echo '[+] Executing flask with Production settings...'
	@echo
	FLASK_APP=flaskr FLASK_ENV=production flask run

init-db:
	@echo
	@echo '[+] Executing flask with DB initialization command...'
	@echo
	FLASK_APP=flaskr FLASK_ENV=production flask init-db

dev-deploy:
	@echo
	@echo '[+] Creating/downloading development version of the app...'
	@echo

.PHONY: run-dev run-prod init-db dev-deploy
