#!/bin/sh

set -a
. ../../../.env.local
set +a

PORT=5000

while getopts p: option; do
   case $option in
      p) # display Help
         echo "Running server on port: ${OPTARG}"
         PORT=${OPTARG};;
      \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done

echo "CHECKING POSTGRES USER"
echo $POSTGRES_USER

gunicorn --bind 0.0.0.0:$PORT wsgi:app