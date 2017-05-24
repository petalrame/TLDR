import React, { Component } from 'react';
import styles from "./Home.css";

import Entry from "../Entry/Entry.js";

class Home extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Home Page</h1>
				<Entry />
			</div>
		);
	}
}

export default Home;
