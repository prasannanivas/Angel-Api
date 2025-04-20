Sure, here's the contents for the file: /stock-tracking-app/stock-tracking-app/client/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import WatchGraph from './components/WatchGraph';
import WatchList from './components/WatchList';
import { AuthProvider } from './context/AuthContext';
import { WebSocketProvider } from './context/WebSocketContext';

const App = () => {
  return (
    <AuthProvider>
      <WebSocketProvider>
        <Router>
          <Switch>
            <Route path="/" exact component={WatchGraph} />
            <Route path="/watchlist" component={WatchList} />
          </Switch>
        </Router>
      </WebSocketProvider>
    </AuthProvider>
  );
};

export default App;