#!/bin/bash

NOTEBOOK_NAME="linearRegression.ipynb"
OUTPUT_NAME="linearRegression.pdf"

jupyter nbconvert --to pdf $NOTEBOOK_NAME --output $OUTPUT_NAME
