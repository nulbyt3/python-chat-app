Overview

A simple terminal-based chat application built with Python's socket module, allowing multiple users to communicate in real-time over a local network or the internet.

Key Features

-Real-time messaging: Instant message delivery between connected clients

-Multi-user support: Multiple clients can connect to the server simultaneously

-Simple interface: Lightweight terminal-based interface

-Customizable: Easy to modify port numbers, host addresses, and other parameters

-Cross-platform: Works on any system with Python installed

How It Works

-The server script creates a socket and listens for incoming connections

-Client scripts connect to the server using the specified IP/port

-Once connected, any message typed by a client is broadcast to all other connected clients

-The server handles message routing and client connections/disconnections

Installation & Usage

-Clone the repository

-Run the server script: python server.py

-Run client scripts in separate terminals: python client.py

-Start chatting!

Technical Details


-Built with Python's built-in socket module

-Uses TCP sockets for reliable communication

-Threading handles multiple client connections simultaneously

-Basic error handling for connection issues

-Perfect for learning socket programming or for quick local network communication!
