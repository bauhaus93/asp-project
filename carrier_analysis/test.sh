#!/bin/bash

for i in `seq 1 8`;
do
  echo "*********** testcase $i ***********"
  dlv -nofacts -silent -N=2 carrier.dl carrier_test$i.dl carrier_test_network.dl
done
