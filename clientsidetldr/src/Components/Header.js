import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Switch, Route } from 'react-router-dom';
import ReactDOM from 'react-dom';

import Home from './Home/Home.js';

const Links = () => 
	<div>
		<nav className="navbar navbar-default">
			<div className="container-fluid">
				<div className="navbar-header">
					<a className="navbar-brand" href="#">TLDR</a>
				</div>
				<div className="collapse navbar-collapse">
					<ul className="nav navbar-nav">
						<li><Link to="/">Home</Link></li>
						<li><Link to="/politics">Politics</Link></li>
						<li><Link to="/economy">Economy</Link></li>
						<li><Link to="/tech">Tech</Link></li>
						<li><Link to="/sports">Sports</Link></li>
						<li><Link to="/fashion">Fashion</Link></li>
						<li><Link to="/crime">Crime</Link></li>
						<li><Link to="/health">Health</Link></li>
					</ul>
				</div>
			</div>
		</nav>
	</div>

class Header extends Component {
	componentDidMount() {
		ReactDOM.render(<Home />, document.getElementById("container"));
		console.log("Component Did Mount in Header.js");
	}
	render() {
		return (
			<Router>
				<div>
					<Switch>
							<Links />
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
					<div id="container"></div>
				</div>
			</Router>
		);
	}
}

export default Header;
