import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import "./Header.css";

function IsLoggedIn(props) {
	let login_status = props.loginStatus;

	if (login_status == 0) {
	//not logged in
		return <Link to="/login"><button className="btn loginbutton">Login</button></Link>
	} else {
		//user is logged in already
		return <button className="btn loginbutton" onClick={props.logout}>Logout</button>
	}
}

class Header extends Component {
	constructor() {
		super();
		this.state = {
			loginstatus: 0
		}		

		this.logout = this.logout.bind(this);
	}
	componentDidMount() {
		console.log("Component Did Mount in Header.js");
		let self = this

		axios.defaults.xsrfCookieName = 'csrftoken'
		axios.defaults.xsrfHeaderName = 'X-CSRFToken'

		axios.get("/api/users/0/login_status/")
		.then(function(response) {
			console.log(response.data)
			let login_status = response.data.login_status;
			console.log(login_status)

			if (login_status == 0) {
				//not logged in
				self.setState({loginstatus: 0});
			} else {
				//user is logged in already
				self.setState({loginstatus: 1});
			}
		}).catch(function (error) {
			console.log(error);
		});
	}
	logout() {
		axios.defaults.xsrfCookieName = 'csrftoken'
		axios.defaults.xsrfHeaderName = 'X-CSRFToken'
		
		axios({
			method: "post",
			url: "/api/users/0/logout/",
			data: {
				username: this.state.username,
				password: this.state.password
			},
		});

		this.setState({loginstatus: 0});
	}
	render() {
		return (
			<div>
				<div className="navbarContainer">
					<nav className="navbar navbar-default">
						<div className="container-fluid">
							<div className="navbar-header">
								<Link to="/" className="navbar-brand">Filtr</Link>
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

							<IsLoggedIn loginStatus={this.state.loginstatus} logout={this.logout} />
						</div>
					</nav>
				</div>
			</div>
		);
	}
}

export default Header;
