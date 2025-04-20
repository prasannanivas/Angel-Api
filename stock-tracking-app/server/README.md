# Stock Tracking App

This project is a stock tracking application that allows users to monitor stock prices in real-time and manage their watchlist. It consists of a client-side built with React and a server-side built with Flask.

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

The client-side of the application is built using React and includes the following components:

- **WatchGraph.js**: Displays a graph for tracking stock prices, manages state for stock data, handles user interactions, and fetches data from the server.
- **WatchList.js**: Displays a list of stocks being tracked, allowing users to add or remove stocks from their watchlist.
- **AuthContext.js**: Provides authentication context for managing user authentication state and secure data fetching.
- **WebSocketContext.js**: Manages WebSocket connections for real-time data updates.

## Server-Side

The server-side is built with Flask and includes the following features:

- **API Endpoints**:
  - `/parse-int64`: Parses an 8-byte array into an int64.
  - `/api/recordTrade`: Records trade transactions in a CSV file.
  - `/api/saveWatchlist`: Saves the user's watchlist to a CSV file.
  - `/api/getWatchlist`: Retrieves the saved watchlist from a CSV file.

- **Data Storage**:
  - **watchlist.csv**: Stores the watchlist of stocks.
  - **trades.csv**: Stores trade records for buy and sell transactions.

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

- Access the client application in your web browser at `http://localhost:3000`.
- Use the watchlist feature to add or remove stocks.
- Monitor stock prices in real-time using the graph component.

## License

This project is licensed under the MIT License.