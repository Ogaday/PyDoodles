#!/bin/bash
# Use to run each of the examples in the scikit-neuralnetwork package.

options=(activation dropout iterations alpha rules units regularize output)
for opt in ${options[*]}; do echo $opt; python scikit-neuralnetwork/examples/plot_mlp.py -p $opt; done