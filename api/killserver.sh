#!/bin/bash


kill $(netstat -tunlp | grep ":8890" | egrep -o "[0-9]+/python" | egrep -o "[0-9]+")

