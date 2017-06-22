import React, { Component } from 'react';
import styles from "./EconomyPage.css";

import Entry from "../../Entry/Entry.js";

class EconomyPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Economy Page</h1>
				<Entry />
			</div>
		);
	}
}

export default EconomyPage;
