GRPC_OUT_FOLDER=proto

create-proto:
	python -m grpc_tools.protoc -I$(GRPC_OUT_FOLDER) --python_out=. --grpc_python_out=. $(GRPC_OUT_FOLDER)/grpc_lib/spec.proto

test-coverage:
	python -m pytest --cov=backend --cov=frontend tests/
	coverage report --fail-under=50

test-coverage-ci:
	QT_QPA_PLATFORM=offscreen make test-coverage

test:
	python -m pytest tests/
ui-create:
	pyuic5 frontend/UI/infection-spread.ui -o frontend/UI/infection_spread_ui.py