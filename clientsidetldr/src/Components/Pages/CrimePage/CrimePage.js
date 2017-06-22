import React, { Component } from 'react';
import styles from "./CrimePage.css";

import Entry from "../../Entry/Entry.js";

class CrimePage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Crime Page</h1>
				<Entry />
			</div>
		);
	}
}

export default CrimePage;
