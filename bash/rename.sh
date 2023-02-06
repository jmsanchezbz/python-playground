#!/bin/bash

for file in *.HTM; do
  name=$(base "$file" .HTM)
  mv "$file" "$name.html"
done