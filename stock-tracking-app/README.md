# Stock Tracking App

## Overview
The Stock Tracking App is a full-stack application that allows users to track stock prices in real-time, manage a watchlist of stocks, and record trades. The application is built using React for the client-side and Flask for the server-side.

## Project Structure
```
stock-tracking-app
├── client
│   ├── src
│   │   ├── components
│   │   │   ├── WatchGraph.js
│   │   │   └── WatchList.js
│   │   ├── context
│   │   │   ├── AuthContext.js
│   │   │   └── WebSocketContext.js
│   │   └── App.js
│   ├── package.json
│   └── README.md
├── server
│   ├── data
│   │   ├── watchlist.csv
│   │   └── trades.csv
│   ├── server.py
│   ├── requirements.txt
│   └── README.md
└── README.md
```

## Client-Side
The client-side of the application is built using React. It includes the following components:
- **WatchGraph.js**: Displays a graph for tracking stock prices and manages state for stock data.
- **WatchList.js**: Displays a list of stocks being tracked and allows users to manage their watchlist.
- **AuthContext.js**: Provides authentication context for managing user authentication state.
- **WebSocketContext.js**: Manages WebSocket connections for real-time data updates.
- **App.js**: The main entry point for the React application.

## Server-Side
The server-side of the application is built using Flask. It includes:
- **server.py**: The main server application that defines API endpoints for parsing data, recording trades, and managing the watchlist.
- **watchlist.csv**: Stores the watchlist of stocks in CSV format.
- **trades.csv**: Stores trade records in CSV format.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-tracking-app
   ```

2. Set up the client:
   ```
   cd client
   npm install
   ```

3. Set up the server:
   ```
   cd server
   pip install -r requirements.txt
   ```

4. Run the server:
   ```
   python server.py
   ```

5. Run the client:
   ```
   cd client
   npm start
   ```

## Usage
- Use the client-side application to add stocks to your watchlist and track their prices in real-time.
- Record trades through the application, which will be saved in the trades.csv file on the server.

## License
This project is licensed under the MIT License.