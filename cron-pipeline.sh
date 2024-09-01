#!/bin/bash

echo $(date -Iseconds) >> /opt/support/pipeline-$(date -I).log 2>& 
/home/ubuntu/pipeline.sh >> /opt/support/pipeline-$(date -I).log 2>&1


