#!/bin/bash
cd example_project
./manage.py jenkins nuit
cd ..
rm -r reports
mv example_project/reports .
