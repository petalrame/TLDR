import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './registerPage.css';

class registerPage extends Component {
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

		<div className={styles.registerContainer}>
			<form className={styles.registerBox} action="/api/users/" method="POST">
				<input className={styles.input_style} name="username" placeholder="Username"></input>
				<input className={styles.input_style} name="email" placeholder="Email"></input>
				<input type="password" className={styles.input_style} name="password" placeholder="Password"></input>
				<input type="password" className={styles.input_style} placeholder="Retype password"></input>
				<input className={"btn " + styles.submit} type="submit" value="Register"></input>
				<Link to="/login" className={styles.loginlink}>Alreadu have an account? Login here</Link>
			</form>
		</div>
	</div>
    );
  }
}

export default registerPage;
