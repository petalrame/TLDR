import React, { Component } from 'react';
import styles from "./PoliticsPage.css";

import Entry from "../../Entry/Entry.js";

class PoliticsPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Politics Page</h1>
				<Entry />
			</div>
		);
	}
}

export default PoliticsPage;
