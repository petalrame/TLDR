import React, { Component } from 'react';
import { Link } from 'react-router-dom';


const Links = () => 
	<div>
		<nav className="navbar navbar-default">
			<div className="container-fluid">
				<div className="navbar-header">
					<Link to="/" className="navbar-brand">TLDR</Link>
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
		console.log("Component Did Mount in Header.js");
	}
	render() {
		return (
			<div>
				<Links />
			</div>
		);
	}
}

export default Header;
