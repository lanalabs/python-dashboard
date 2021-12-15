#!/usr/bin/env bash

set -e

# TODO Remove secrets
DASHBOARD_NAME="csimple"
ASSETSRC="simple_dashboard"
LOG_ID="3fc2d6e5-c9b8-4f5f-9167-8a6691a4b469"
API_KEY="abbbed8d6f5544c9873ee353d95d2fe4"
URL="http://localhost:4000"
ASSET="../upload.zip"

while [ 1 ]; do
  rm -f $ASSET
  pushd $ASSETSRC
  zip -r $ASSET *
  popd

  DASHBOARD_ID=$(curl -X POST ${URL}/api/v2/custom-dashboards \
                      -H "Authorization: API-Key ${API_KEY}" \
                      -H "Content-Type: application/json" \
                      --data-raw '{
    "name": "csimple",
    "type": "python_dashboard"
  }' | jq -r .id)

  echo "Advanced dashboard id: ${DASHBOARD_ID}"

  echo "Uploading ..."

  curl -X POST ${URL}/api/v2/custom-dashboards/${DASHBOARD_ID}/source \
       -H "Authorization: API-Key ${API_KEY}" \
       -F file=@"./upload.zip"

  echo "Connecting ..."

  curl -X POST ${URL}/api/v2/resource-connections \
       -H "Authorization: API-Key ${API_KEY}" \
       -H "Content-Type: application/json" \
       --data-raw '{
    "log_id":"'"${LOG_ID}"'",
    "custom_dashboard_id":"'"${DASHBOARD_ID}"'"
  }' 1>/dev/null

  echo
  echo "Either press Ctrl-C to interrupt _or_ ENTER to clean up and move on!"

  read

  echo "DELETING dashboard ..."

  curl -X DELETE ${URL}/api/v2/custom-dashboards/${DASHBOARD_ID} \
                    -H "Authorization: API-Key ${API_KEY}" \
                    -H "Content-Type: application/json"

  echo "Press Enter to move on!"
  read
done

exit 0
