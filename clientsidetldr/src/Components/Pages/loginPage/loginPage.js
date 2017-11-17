import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './loginPage.css';

class loginPage extends Component {
  render() {
    return (
	<div>
		<div>
			<nav className={"navbar navbar-default " + styles.nav}>
				<div className={"container-fluid " + styles.navbar}>
					<h1>Filtr</h1>
				</div>
			</nav>
		</div>

		<div className={styles.loginContainer}>
			<form className={styles.loginBox} action="/api/users/0/login/" method="POST">
				<input className={styles.input_style} name="username" placeholder="Username"></input>
				<input type="password" className={styles.input_style} name="password" placeholder="Password"></input>
				<input className={"btn " + styles.submit} type="submit" value="Login" onClick={this.login}></input>
				<Link to="/register" className={styles.registerlink}>Don't have an account yet? Register here</Link>
			</form>
		</div>
	</div>
    );
  }
}

export default loginPage;
