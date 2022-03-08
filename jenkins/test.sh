#!/bin/bash

echo "Test stage"


# venv created, sourced
python3 -m venv venv
source venv/bin/activate

#install pip3 dependencies
pip3 install -r requirements.txt


#run pytest frontend
python3 -m pytest \
--cov=application \
--cov-report term-missing \
--cov-report xml:test_reports/frontend_coverage.xml \
--junitxml=test_reports/frontend_junit_report.xml

#run pytest backend
python3 -m pytest backend \
--cov=backend/application \
--cov-report term-missing \
--cov-report html


#remove venv
deactivate
rm -rf venv