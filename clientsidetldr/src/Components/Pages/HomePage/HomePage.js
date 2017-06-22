import React, { Component } from 'react';
import styles from "./HomePage.css";

import Entry from "../../Entry/Entry.js";

class HomePage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>HomePage</h1>
				<Entry />
			</div>
		);
	}
}

export default HomePage;
