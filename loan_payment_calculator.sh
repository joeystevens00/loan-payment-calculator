#!/bin/bash
docker build -t loan_payment_calculator:latest . > /dev/null
docker run -i loan_payment_calculator <&0
