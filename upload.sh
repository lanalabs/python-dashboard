#!/usr/bin/env bash

API_KEY="<API_KEY>"
DASHBOARD_ID="<DASHBOARD_ID>"
URL="<URL>"

rm upload.zip
cd dashboard; zip -r ../upload.zip *; cd ..

curl -X POST "${URL}/api/v2/custom-dashboards/${DASHBOARD_ID}/source" \
  -H "Authorization: API-Key ${API_KEY}" \
  -F file=@"upload.zip"
