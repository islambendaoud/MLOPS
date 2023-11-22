# Makefile

.PHONY: build_dev_requirements install_dev_requirements install install_packages

build_dev_requirements:
    @echo "Building development requirements..."
    pip-compile requirements.in

install_dev_requirements: build_dev_requirements
    @echo "Installing development requirements..."
    pip install -r requirements.txt

install: install_dev_requirements
    @echo "Installing your package..."


install_packages : pip install -e .
