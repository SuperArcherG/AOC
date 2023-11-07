#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

echo "\nAdvent of Code 2022 - All Answers\n"
cd 2022

echo "Day 1"
cd 1
start_time=$(date +%s%N)
dotnet build -c Release > /dev/null 2>&1
dotnet run bin/Release/net7.0/AOC1.dll
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 2"
cd ../2
start_time=$(date +%s%N)
dotnet build -c Release > /dev/null 2>&1
dotnet run bin/Release/net7.0/AOC2.dll
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 3"
cd ../3
start_time=$(date +%s%N)
python3 main.py
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 4"
cd ../4
start_time=$(date +%s%N)
python3 main.py
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 5"
cd ../5
start_time=$(date +%s%N)
python3 main.py
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 6"
cd ../6
start_time=$(date +%s%N)
python3 main.py
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 7"
cd ../7
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 8"
cd ../8
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 9"
cd ../9
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 10"
cd ../10
start_time=$(date +%s%N)
dotnet build -c Release > /dev/null 2>&1
dotnet run bin/Release/net7.0/AOC10.dll
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 11"
cd ../11
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 12"
cd ../12
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 13"
cd ../13
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 14"
cd ../14
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 15"
cd ../15
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 16"
cd ../16
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 17"
cd ../17
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 18"
cd ../18
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 19"
cd ../19
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 20"
cd ../20
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 21"
cd ../21
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 22"
cd ../22
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 23"
cd ../23
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 24"
cd ../24
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"

echo "Day 25"
cd ../25
start_time=$(date +%s%N)
echo "$((($(date +%s%N | tr -d ',') - start_time) / 1000000))ms\n"