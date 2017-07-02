import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./HealthPage.css";

import Entry from "../../Entry/Entry.js";

class HealthPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/health/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default HealthPage;
