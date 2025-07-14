#!/bin/bash

echo "Choose an option:"
echo "1. Sign in with QR Code"
echo "2. Run API"
read -p "Enter your choice (1 or 2), use CTRL-C to close it: " choice

case $choice in
    1)
        echo "Running Signal CLI in normal mode for QR code sign-in..."
        docker run -p 8080:8080 \
            -v "$(pwd)/signal-cli-config:/home/.local/share/signal-cli" \
            -e 'MODE=normal' bbernhard/signal-cli-rest-api:latest
        ;;
    2)
        echo "Running Signal CLI in JSON-URL mode for API..."
        docker run -p 8080:8080 \
            -v "$(pwd)/signal-cli-config:/home/.local/share/signal-cli" \
            -e 'MODE=json-url' bbernhard/signal-cli-rest-api:latest
        ;;
    *)
        echo "Invalid choice. Please enter 1 or 2."
        ;;
esac