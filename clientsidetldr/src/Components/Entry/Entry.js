import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Link } from 'react-router-dom';

import styles from "./Entry.css";
import pic from "./images/cat3.jpg";
import upPic from "./images/chevron-up.png";
import downPic from "./images/chevron-down.png";

class Entry extends Component {
	onClick() {
		console.log("Entry clicked");
	}
	render() {
		return(
			<Router>
			<div className={styles.outerbox}>
				<div className={styles.likebox}>
					<img className={styles.like} src={upPic} alt="Not Available"></img>
					<img className={styles.like} src={downPic} alt="Not Available"></img>
				</div>
				<img src={pic} className={styles.pic} alt="Not Available"></img>
				<div className={styles.description}>
					<Link to="cat" className={styles.link} onClick={() => this.onClick()}>
						<h2>Title goes here</h2>
					</Link>
					<p className={styles.textDescription}>Description Goes Here</p>
				</div>
			</div>
			</Router>
		);
	}
}

export default Entry;
