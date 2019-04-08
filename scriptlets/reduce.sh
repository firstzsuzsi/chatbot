#! /bin/bash

< /dev/stdin jq '(reduce .str as $stringy (""; .+"nyeh"))'
