#!/bin/bash
# A sample Bash build script that include the jar

cd src
javac -cp ".:xchart-3.5.4.jar:" *.java