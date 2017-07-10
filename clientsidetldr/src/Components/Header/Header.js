import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import "./Header.css";

const Links = () => 
	<div>
		<nav className="navbar navbar-default">
			<div className="container-fluid">
				<div className="navbar-header">
					<Link to="/" className="navbar-brand">TLDR</Link>
				</div>
				<div className="collapse navbar-collapse">
					<ul className="nav navbar-nav">
						<li><Link to="/politics" className="link">Politics</Link></li>
						<li><Link to="/economy" className="link">Economy</Link></li>
						<li><Link to="/tech" className="link">Tech</Link></li>
						<li><Link to="/sports" className="link">Sports</Link></li>
						<li><Link to="/fashion" className="link">Fashion</Link></li>
						<li><Link to="/crime" className="link">Crime</Link></li>
						<li><Link to="/health" className="link">Health</Link></li>
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
