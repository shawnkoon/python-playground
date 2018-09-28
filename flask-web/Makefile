run-dev:
	@cho
	@echo 'Executing flask with Development settings...'
	FLASK_APP=flaskr FLASK_ENV=development flask run
	@echo

run-prod: init-db
	@echo
	@echo 'Executing flask with Production settings...'
	FLASK_APP=flaskr FLASK_ENV=production flask run
	@echo

init-db:
	@echo
	@echo 'Executing flask with DB initialization command...'
	FLASK_APP=flaskr FLASK_ENV=production flask init-db
	@echo

dev-deploy:
	@echo
	@echo 'Creating/downloading development version of the app...'
	@echo

.PHONY: run-dev run-prod init-db dev-deploy
