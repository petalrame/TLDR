import React, { Component } from 'react';
import styles from "./FashionPage.css";

import Entry from "../../Entry/Entry.js";

class FashionPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<h1>Fashion Page</h1>
				<Entry />
			</div>
		);
	}
}

export default FashionPage;
