# Stock Tracking App

This project is a stock tracking application that allows users to monitor stock prices in real-time and manage their watchlist of stocks. The application is divided into two main parts: the client-side built with React and the server-side built with Flask.

## Client

The client-side of the application is responsible for the user interface and user interactions. It includes the following components:

- **WatchGraph.js**: A React component that displays a graph for tracking stock prices. It manages state for stock data, handles user interactions, and fetches data from the server.
  
- **WatchList.js**: A React component that displays a list of stocks being tracked. It allows users to add or remove stocks from their watchlist.

### Contexts

- **AuthContext.js**: Provides authentication context for the application, managing user authentication state and providing methods for fetching data securely.

- **WebSocketContext.js**: Manages WebSocket connections for real-time data updates. It provides context for subscribing and unsubscribing to market data.

### Main Entry Point

- **App.js**: The main entry point for the React application. It sets up routing and renders the main components.

### Package Configuration

- **package.json**: The configuration file for npm. It lists the dependencies and scripts for the client-side application.

## Server

The server-side of the application handles API requests and manages data storage. It includes the following features:

- **watchlist.csv**: Stores the watchlist of stocks in CSV format, allowing the server to read and write stock data.

- **trades.csv**: Stores trade records in CSV format, keeping track of buy and sell transactions.

### Server Application

- **server.py**: The main server application built with Flask. It defines API endpoints for parsing data, recording trades, saving and retrieving the watchlist, and handling CORS.

### Requirements

- **requirements.txt**: Lists the Python dependencies required for the server application.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd stock-tracking-app
   ```

2. **Install client dependencies**:
   ```bash
   cd client
   npm install
   ```

3. **Run the client application**:
   ```bash
   npm start
   ```

4. **Install server dependencies**:
   ```bash
   cd server
   pip install -r requirements.txt
   ```

5. **Run the server application**:
   ```bash
   python server.py
   ```

## Usage

- Access the client application in your web browser at `http://localhost:3000`.
- The server API will be running at `http://localhost:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.