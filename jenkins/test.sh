#!/bin/bash

echo "Test stage"

# venv created, sourced
python3 -m venv venv
source venv/bin/activate

#install pip3 dependencies
pip3 install -r requirements.txt

rm -rf test_reports

#run pytest 
python3 -m pytest \
--cov=application \
--cov-report term-missing \
--cov-report html


#remove venv
deactivate
rm -rf venv
