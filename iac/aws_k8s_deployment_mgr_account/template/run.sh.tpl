#!/bin/bash

export current_dir=$(pwd)
cd ../ftl-python-lib/ && poetry install
alembic upgrade head
cd $current_dir
flask run
