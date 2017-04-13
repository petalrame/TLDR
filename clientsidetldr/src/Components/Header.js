import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Switch, Route } from 'react-router-dom'

import Home from './Home'

const Links = () => 
	<nav>
		<li><Link to="/">Home</Link></li>
		<li><Link to="/politics">Politics</Link></li>
		<li><Link to="/economy">Economy</Link></li>
		<li><Link to="/tech">Tech</Link></li>
		<li><Link to="/sports">Sports</Link></li>
		<li><Link to="/fashion">Fashion</Link></li>
		<li><Link to="/crime">Crime</Link></li>
		<li><Link to="/health">Health</Link></li>
	</nav>

class Header extends Component {
	render() {
		return (
			<Router>
				<div style={divStyle}>
					<h1>TLDR</h1>
					<Links />
					<Switch>
						<Route exact path="/" component={Home} />
						<Route exact path="/politics" render={() => <h1>Politics</h1>} />
						<Route exact path="/economy" render={() => <h1>Economy</h1>} />
						<Route exact path="/tech" render={() => <h1>Tech</h1>} />
						<Route exact path="/sports" render={() => <h1>Sports</h1>} />
						<Route exact path="/fashion" render={() => <h1>Fashion</h1>} />
						<Route exact path="/crime" render={() => <h1>Crime</h1>} />
						<Route exact path="/health" render={() => <h1>Health</h1>} />
					<Route render={() => <h1>Home</h1>} />
					</Switch>
				</div>
			</Router>
		);
	}
}

const divStyle = {
	backgroundColor: 'grey'
}

export default Header;
