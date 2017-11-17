import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import styles from "./App.css"

import Index from './Components/Index.js';
import loginPage from './Components/Pages/loginPage/loginPage.js';
import registerPage from './Components/Pages/registerPage/registerPage.js';

class App extends Component {
  render() {
    return (
	<Router>
		<div>
			<Switch>
				<Route path="/login" component={loginPage} />
				<Route path="/register" component={registerPage} />
				<Route path="/*" component={Index} />
			</Switch>
		</div>
	</Router>
    );
  }
}

export default App;
