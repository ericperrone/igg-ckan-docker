#!/bin/sh
set -e

# Aspetta che il database sia pronto (opzionale ma consigliato)
# ./wait-for-it.sh db:5432 -t 60

# Avvia CKAN
echo "Starting ckan"
exec /srv/app/start_ckan.sh

# Aggiorna il DB per ckanext-doi
echo "Executing command ckan -c /srv/app/ckan.ini db upgrade -p doi"
ckan -c /srv/app/ckan.ini db upgrade -p doi
