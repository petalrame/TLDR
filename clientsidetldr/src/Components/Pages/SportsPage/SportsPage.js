import React, { Component } from 'react';
import styles from "./SportsPage.css";

import Entry from "../../Entry/Entry.js";

class SportsPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Sports Page</h1>
				<Entry />
			</div>
		);
	}
}

export default SportsPage;
