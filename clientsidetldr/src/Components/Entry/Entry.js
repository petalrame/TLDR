import React, { Component } from 'react';
import axios from 'axios';

import styles from "./Entry.css";
import pic from "../images/cat3.jpg";

class Entry extends Component {
	constructor(props) {
		super(props);
		this.state = {
			idVal: this.props.idval,
			upselected: false,
			downselected: false,
			likeCount: this.props.ranking
		}
	}
	onClick() {
		console.log("Entry clicked");
	}
	likeButtonClicked(buttonNumb) {
		let previousLikeState = this.state.likeCount;	//like Count before update

		if (buttonNumb == 1) {
			//up button was clicked
			if (!this.state.upselected) {
				if (this.state.downselected) {
					this.setState({
						upselected: true,
						downselected: false,
						likeCount: this.state.likeCount + 2
					});
				} else {
					this.setState({
						upselected: true,
						downselected: false,
						likeCount: this.state.likeCount + 1
					});
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

				} else {
					this.setState({
						upselected: false,
						downselected: true,
						likeCount: this.state.likeCount - 1
					});
				}
			}
		}
		
		axios({
			method: "post",
			url: "/api/" + this.state.idVal + "/like/",
			data: {
				likestatus: this.state.likeCount - previousLikeState 
			},
			xsrfHeaderName: "X-CSRFToken",
		});
	}
	likeBoxClick(e) {
		e.preventDefault();
	}
	render() {
		return(
			<div className={styles.outerbox}>
				<div className={styles.likebox} onClick={this.likeBoxClick}>
					<div>
						<span className={"glyphicon glyphicon-chevron-up " + styles.like + " " + (this.state.upselected ? styles.likeselected:'')}
							onClick={() => this.likeButtonClicked(1)}></span>
						<span className={"glyphicon glyphicon-chevron-down " + styles.like + " " + (this.state.downselected ? styles.likeselected:'')}
							onClick={() => this.likeButtonClicked(2)}></span>
					</div>
					<span className={styles.likeCount}>{this.state.likeCount}</span>
				</div>
				<img src={pic} className={styles.pic} alt="Not Available"></img>
				<div className={styles.description}>
					<h2 className={styles.link}>{this.props.title}</h2>
					<p className={styles.textDescription}>{this.props.summary}</p>
				</div>
			</div>
		);
	}
}

export default Entry;
