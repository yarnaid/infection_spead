create-proto:
	python -m grpc_tools.protoc -IgRPC --python_out=gRPC --grpc_python_out=gRPC gRPC/spec.proto
test-coverage:
	python -m pytest --cov=backend --cov=frontend tests/

test:
	python -m pytest tests/
ui-create:
	pyuic5 frontend/UI/infection-spread.ui -o frontend/UI/infection_spread_ui.py