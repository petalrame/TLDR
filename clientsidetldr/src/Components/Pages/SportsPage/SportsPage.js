import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./SportsPage.css";

import Entry from "../../Entry/Entry.js";

class SportsPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/sports/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default SportsPage;
