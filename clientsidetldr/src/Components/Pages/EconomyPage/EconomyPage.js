import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./EconomyPage.css";

import Entry from "../../Entry/Entry.js";

class EconomyPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/economy/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default EconomyPage;
