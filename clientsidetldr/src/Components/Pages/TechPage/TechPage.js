import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./TechPage.css";

import Entry from "../../Entry/Entry.js";

class TechPage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/tech/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default TechPage;
