import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./PoliticsPage.css";

import Entry from "../../Entry/Entry.js";

class PoliticsPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/politics/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default PoliticsPage;
