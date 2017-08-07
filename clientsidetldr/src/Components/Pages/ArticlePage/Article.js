import React, { Component } from 'react';
import styles from "./Article.css";

import catPic from "../images/cat4.png";
import twitter_logo from "./logos/twitter_logo.png";
import Comments from "./Comments/Comments.js";
import upPic from "../../images/chevron-up.png";
import downPic from "../../images/chevron-down.png";


class Article extends Component {
	constructor() {
		super();
		this.state = {
			pageContent: [],
		}
	}
	componentDidMount() {
		console.log(location.href);
		let self = this;
		fetch("http://localhost:3000/entries/" + this.props.match.params.number).then(function(response) {
			var contentType = response.headers.get("content-type");
			if (contentType && contentType.includes("application/json")) {
				return response.json();
			}
			throw new TypeError("Error: Didn't receive JSON");
		}).then(function(json) {
			console.log(json);
			self.setState({
				pageContent: json
			});
			console.log(self.state.pageContent)
		}).catch(function(error) {
			console.log(error);
		});

	}
	twitterShare() {
		//share page on twitter, Popup in middle of screen
		var w = 800;
		var h = 600;
		var dualScreenLeft = window.screenLeft != undefined ? window.screenLeft : screen.left;
    		var dualScreenTop = window.screenTop != undefined ? window.screenTop : screen.top;

    		var width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    		var height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

    		var left = ((width / 2) - (w / 2)) + dualScreenLeft;
    		var top = ((height / 2) - (h / 2)) + dualScreenTop;
    		var newWindow = window.open("https://twitter.com/share", "Twitter Share", 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);
	}
	render() {
		console.log(this.props.match.params.number);
		return(
			<div className={styles.outerbox}>
				<h1 className={styles.title}>{this.state.pageContent.title}</h1>

				<div className={styles.infoBox}>
					<img src={catPic} className={styles.Image} alt="Article Image"></img>
					<div className={styles.pageInfoBox}>
						<p>Event Published on (Insert Date)</p>
						<p>Event Last Edited on (Insert Date)</p>
						
						<div className={styles.socialMediaBox}>
							<div className="fb-share-button" data-href={location.href} data-layout="button_count" data-size="large" data-mobile-iframe="false"><a className="fb-xfbml-parse-ignore" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse">Share</a></div>
							<img className={styles.logo} src={twitter_logo} onClick={this.twitterShare}></img>
						</div>

						<div className={styles.likeBoxContainer}>
							<div className={styles.likeBox}>
								<span className={"glyphicon glyphicon-chevron-up " + styles.like}></span>
								<span className={"glyphicon glyphicon-chevron-down " + styles.like}></span>
							</div>
							<h3 className={styles.likeCount}>0</h3>
						</div>
					</div>
				</div>

				
				<div className={styles.wordContent}>
					<p>{this.state.pageContent.summary}</p>
				</div>
				<Comments />
			</div>
		);
	}
}

export default Article;
