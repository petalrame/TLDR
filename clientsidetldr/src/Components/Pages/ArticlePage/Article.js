import React, { Component } from 'react';
import styles from "./Article.css";

class Article extends Component {
	render() {
		console.log("We here");
		return(
			<div className={styles.outerbox}>
				<h3>Article Title</h3>
				<p>Article Content</p>
			</div>
		);
	}
}

export default Article;
