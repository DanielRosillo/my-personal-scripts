#!/usr/bin/env bash
trap 'read -p "[$BASH_SOURCE:$LINENO] $BASH_COMMAND"' DEBUG

echo "Foo"
echo "Bar"
echo "Baz"