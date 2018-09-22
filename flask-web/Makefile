run-dev:
	@echo 'Executing flask with Development settings...'
	FLASK_APP=flaskr FLASK_ENV=development flask run

run-prod:
	@echo 'Executing flask with Production settings...'
	FLASK_APP=flaskr FLASK_ENV=production flask run

init-db:
	@echo 'Executing flask with DB initialization command...'
	FLASK_APP=flaskr FLASK_ENV=production flask init-db

.PHONY: run-dev run-prod init-db
