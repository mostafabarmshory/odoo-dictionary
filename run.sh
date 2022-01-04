#!/bin/bash

DATA_FOLDER=data
if [ ! -d "$DATA_FOLDER" ]; then
	mkdir "$DATA_FOLDER"
	chmod 777 data
fi


DB_FOLDER=postgresql
if[ ! -d "$DB_FOLDER" ]; then
	mkdir "$DB_FOLDER"
	chmod 777
fi

docker-compose up
