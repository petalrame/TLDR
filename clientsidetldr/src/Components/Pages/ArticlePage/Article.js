import React, { Component } from 'react';
import styles from "./Article.css";

import catPic from "../images/cat4.png";
import Comments from "./Comments/Comments.js";

class Article extends Component {
	render() {
		console.log(this.props.match.params.number);
		return(
			<div className={styles.outerbox}>
				<h3>Article Title</h3>
				<img src={catPic} alt="Article Image"></img>

				<div>
				</div>

				<p>Will be pulled from database</p>
				<Comments />
			</div>
		);
	}
}

export default Article;
