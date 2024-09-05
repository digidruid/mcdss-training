#!/bin/bash


kill $(netstat -tunlp | grep ":8899" | egrep -o "[0-9]+/python" | egrep -o "[0-9]+")

