import React, { Component } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import styles from "./App.css"

import Index from './Components/Index.js';
import Header from './Components/Header/Header.js';

class App extends Component {
  render() {
    return (
	<Router>
		<div>
			<Header />
			<div className={styles.filler}></div>
			<Index />
		</div>
	</Router>
    );
  }
}

export default App;
