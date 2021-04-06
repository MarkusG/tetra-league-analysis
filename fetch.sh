#!/bin/bash

curl 'https://ch.tetr.io/api/users/lists/league/all' | jq -c .data.users > data.json
