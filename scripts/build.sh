#!/usr/bin/env bash

ROOT=$(git rev-parse --show-toplevel)

cd $ROOT && docker build -t pppj-music $ROOT
