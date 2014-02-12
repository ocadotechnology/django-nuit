#!/bin/bash
cd test_project
./manage.py jenkins nuit
cd ..
rm -r reports
mv test_project/reports .
