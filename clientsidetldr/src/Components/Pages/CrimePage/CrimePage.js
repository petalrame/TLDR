import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./CrimePage.css";

import Entry from "../../Entry/Entry.js";

class CrimePage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/crime/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default CrimePage;
