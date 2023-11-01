#!/bin/bash

rm -rf PRSA_Data_*.csv
gsutil -m cp -r gs://data.datastack.academy/beijing_airquality/*.csv .
