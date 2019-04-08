#! /bin/bash

# < /dev/stdin jq -s '.[]'
# < /dev/stdin jq -s '.[].entities[] | map(type)'
# < /dev/stdin jq '.base | map(.+.*.)'
< /dev/stdin jq '.str | map(.+" okay")'
