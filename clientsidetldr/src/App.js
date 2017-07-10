import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';

import Index from './Components/Index.js';
import Header from './Components/Header/Header.js';

class App extends Component {
  render() {
    return (
	<Router>
		<div>
			<Header />
			<Index />
		</div>
	</Router>
    );
  }
}

export default App;
