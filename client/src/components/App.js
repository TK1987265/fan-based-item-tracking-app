import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Navbar';
import Locations from './Locations';
import Items from './Items';
import LocationItems from './LocationItems';
import Home from './Home';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/locations" component={Locations} />
        <Route path="/items" component={Items} />
        <Route path="/location-items" component={LocationItems} />
      </Switch>
    </Router>
  );
}

export default App;
