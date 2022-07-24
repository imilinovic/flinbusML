#!/bin/bash

gunicorn -c gunicorn_config.py service.service:app
