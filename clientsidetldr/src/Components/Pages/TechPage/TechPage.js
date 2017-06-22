import React, { Component } from 'react';
import styles from "./TechPage.css";

import Entry from "../../Entry/Entry.js";

class TechPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Tech Page</h1>
				<Entry />
			</div>
		);
	}
}

export default TechPage;
