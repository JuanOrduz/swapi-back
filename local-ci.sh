#!/bin/bash
apps="swapi app"
isort $(echo $apps)
black $(echo $apps)
flake8 $(echo $apps)
