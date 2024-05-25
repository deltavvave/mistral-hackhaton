#!/bin/bash

start_services() {
    echo "Starting services..."
    if [ -d "interface" ]; then
        cd interface
        python -m http.server 8000 &
        cd ..
    else
        echo "Error: 'interface' directory not found."
        exit 1
    fi

    if [ -f "interface/whisper.cpp/command" ]; then
        interface/whisper.cpp/command -m interface/whisper.cpp/models/ggml-tiny.en.bin -t 4 &
    else
        echo "Error: 'whisper.cpp/command' not found."
        exit 1
    fi
}

stop_services() {
    echo "Stopping services..."
    pkill -f "python -m http.server 8000"
    pkill -f "interface/whisper.cpp/command -m interface/whisper.cpp/models/ggml-tiny.en.bin -t 4"
}

if [ "$1" == "start" ]; then
    start_services
elif [ "$1" == "stop" ]; then
    stop_services
else
    echo "Usage: $0 [start|stop]"
    exit 1
fi