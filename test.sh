#!/bin/bash
cd test_project
./manage.py jenkins nuitng
cd ..
rm -r reports
mv test_project/reports .
