import React, { Component } from 'react';

import styles from "./Entry.css";
import pic from "../images/cat3.jpg";
import upPic from "../images/chevron-up.png";
import downPic from "../images/chevron-down.png";

class Entry extends Component {
	constructor() {
		super();
	}
	onClick() {
		console.log("Entry clicked");
	}
	render() {
		return(
			<div className={styles.outerbox}>
				<div className={styles.likebox}>
					<img className={styles.like} src={upPic} alt="Not Available"></img>
					<img className={styles.like} src={downPic} alt="Not Available"></img>
				</div>
				<img src={pic} className={styles.pic} alt="Not Available"></img>
				<div className={styles.description}>
					<h2 className={styles.link}>{this.props.title}</h2>
					<p className={styles.textDescription}>Description Goes Here</p>
				</div>
			</div>
		);
	}
}

export default Entry;
