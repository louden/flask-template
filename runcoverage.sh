#! /usr/bin/env sh

py.test -s --cov-report term-missing --cov-config tests/.coveragerc --cov app tests/