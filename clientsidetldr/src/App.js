import React, { Component } from 'react';
import Header from './Components/Header';
import Article from './Components/Article';

class App extends Component {
  render() {
    return (
      <div className="App">
		<Header />
		<Article />
      </div>
    );
  }
}

export default App;
