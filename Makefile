help:           ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

create-proto:  ## generate python grpc libraries
	python -m grpc_tools.protoc -IgRPC --python_out=gRPC --grpc_python_out=gRPC gRPC/spec.proto

test-coverage: ## run pytest with coverage
	python -m pytest --cov=backend --cov=frontend tests/
	coverage report --fail-under=50

test:  ## run pytest
	python -m pytest tests/

ui-create:  ## regenerate python UI files
	pyuic5 frontend/UI/infection-spread.ui -o frontend/UI/infection_spread_ui.py