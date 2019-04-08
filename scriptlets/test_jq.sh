#!/bin/bash
< /dev/stdin jq -s '
.[]
  | (reduce .entities[] as $entity (""; . + "," + $entity.value)) as $entityStr
  | "\(.intent.name),\(.intent.confidence)\($entityStr)"
'
