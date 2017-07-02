import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./HomePage.css";

import Entry from "../../Entry/Entry.js";

class HomePage extends Component {
	render() {
		return(
			<div className={styles.home}>
				<Link to="/1">
					<Entry />
				</Link>
			</div>
		);
	}
}

export default HomePage;
