#!/bin/bash

input="${1}"

maybe() {
    if [ -z "${1}" ]; then
        printf "variable empty\n"
        exit 1
    else
        printf "\n$1\n"
    fi
    printf "this only prints if variable is not null\n"
}

maybe "${input}"