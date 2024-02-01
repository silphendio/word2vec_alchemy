#!/bin/sh

if [ ! -r "glove.6B.300d.txt" ]; then
    wget https://nlp.stanford.edu/data/glove.6B.zip
    unzip glove.6B.zip
fi


unzip glove.6B.zip
