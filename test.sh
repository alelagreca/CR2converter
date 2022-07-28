#!/bin/bash

input="${1}"

maybe() {
    if [ -z "${1}" ]; then
        printf "variable empty\n"
        exit 1
    else
        printf "$1\n"
    fi
    printf "this only prints if variable is not null\n"
}

export -f maybe

maybe "${input}"