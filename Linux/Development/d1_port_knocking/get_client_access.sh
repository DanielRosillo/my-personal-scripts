#!/bin/bash

# Knock sequence
curl -sk https://example.mx > /dev/null
sleep 1
curl -sk https://example.mx:85/two.html > /dev/null
sleep 1
curl -sk https://example.mx:90/tree.html > /dev/null
