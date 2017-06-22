import React, { Component } from 'react';
import styles from "./HealthPage.css";

import Entry from "../../Entry/Entry.js";

class HealthPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Health Page</h1>
				<Entry />
			</div>
		);
	}
}

export default HealthPage;
