import React, { Component } from 'react';
import axios from 'axios';
import styles from "./Article.css";

import catPic from "../images/cat4.png";
import twitter_logo from "./logos/twitter_logo.png";
import Comments from "./Comments/Comments.js";
import upPic from "../../images/chevron-up.png";
import downPic from "../../images/chevron-down.png";
import imageNotAvailable from "../images/image_not_available.png";


class Article extends Component {
	constructor() {
		super();
		this.state = {
			pageContent: [],
			upselected: false,
			downselected: false,
			likeCount: 0
		}
	}
	componentDidMount() {
		console.log(location.href);
		let self = this;
		fetch("api/" + this.props.match.params.number + "/get_entry/").then(function(response) {
			var contentType = response.headers.get("content-type");
			if (contentType && contentType.includes("json")) {
				return response.json();
			}
			throw new TypeError("Error: Didn't receive JSON");
		}).then(function(json) {
			console.log(json);
			self.setState({
				pageContent: json,
				likeCount: json.ranking
			});
			console.log(self.state.pageContent)
		}).catch(function(error) {
			console.log(error);
		});

		(function(d, s, id) {	//for facebook share button
  			var js, fjs = d.getElementsByTagName(s)[0];
  			if (d.getElementById(id)) return;
  			js = d.createElement(s); js.id = id;
  			js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.10";
  			fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));

		window.twttr = (function(d, s, id) {	//for twitter share button
			var js, fjs = d.getElementsByTagName(s)[0],
			t = window.twttr || {};
  			if (d.getElementById(id)) return t;
  			js = d.createElement(s);
			js.id = id;
			js.src = "https://platform.twitter.com/widgets.js";
			fjs.parentNode.insertBefore(js, fjs);

			t._e = [];
			t.ready = function(f) {
				t._e.push(f);
			};

			return t;
		}(document, "script", "twitter-wjs"));
	}
	likeButtonClicked(buttonNumb) {
		var likeStatusChange = 0

		if (buttonNumb == 1) {
			//up button was clicked
			if (!this.state.upselected) {
				if (this.state.downselected) {
					this.setState({
						upselected: true,
						downselected: false,
						likeCount: this.state.likeCount + 2
					});
					likeStatusChange = 2
				} else {
					this.setState({
						upselected: true,
						downselected: false,
						likeCount: this.state.likeCount + 1
					});
					likeStatusChange = 1
				}
			}
		} else {
			//down button was clicked
			if (!this.state.downselected) {
				if (this.state.upselected) {
					this.setState({
						upselected: false,
						downselected: true,
						likeCount: this.state.likeCount - 2
					});
					likeStatusChange = -2

				} else {
					this.setState({
						upselected: false,
						downselected: true,
						likeCount: this.state.likeCount - 1
					});
					likeStatusChange = -1
				}
			}
		}

		axios.defaults.xsrfCookieName = 'csrftoken'
		axios.defaults.xsrfHeaderName = 'X-CSRFToken'
		
		axios({
			method: "post",
			url: "/api/" +  this.props.match.params.number + "/like/",
			data: {
				likestatus: likeStatusChange 
			},
		});
	}
	render() {
		console.log(this.props.match.params.number);
		return(
			<div className={styles.outerbox}>
				<h1 className={styles.title}>{this.state.pageContent.title}</h1>

				<div className={styles.infoBox}>
					<img src={imageNotAvailable} className={styles.Image} alt="Article Image"></img>
					<div className={styles.pageInfoBox}>
						<p>Event Published on (Insert Date)</p>
						<p>Event Last Edited on (Insert Date)</p>
						
						<div className={styles.socialMediaBox}>
							<div className="fb-share-button" data-href={location.href} data-layout="button_count" data-size="large" data-mobile-iframe="false"><a className="fb-xfbml-parse-ignore" target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse">Share</a></div>
							<a className="twitter-share-button" href="https://twitter.com/intent/tweet">Tweet</a>
						</div>

						<div className={styles.likeBoxContainer}>
							<div className={styles.likeBox}>
								<span className={"glyphicon glyphicon-chevron-up " + styles.like + " " + (this.state.upselected ? styles.likeselected:'')}
									onClick={() => this.likeButtonClicked(1)}></span>
								<span className={"glyphicon glyphicon-chevron-down " + styles.like + " " + (this.state.downselected ? styles.likeselected:'')}
									onClick={() => this.likeButtonClicked(2)}></span>
							</div>
							<h3 className={styles.likeCount}>{this.state.likeCount}</h3>
						</div>
					</div>
				</div>

				
				<div className={styles.wordContent}>
					<p>{this.state.pageContent.summary}</p>
				</div>
			</div>
		);
	}
}

export default Article;
