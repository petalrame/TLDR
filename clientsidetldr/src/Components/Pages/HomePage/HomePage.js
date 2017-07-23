import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from "./HomePage.css";

import Entry from "../../Entry/Entry.js";

class HomePage extends Component {
	constructor() {
		super();
		this.state = {
			content: [],
		}
	}
	componentDidMount() {
		let self = this;

		fetch("http://localhost:3000/entries").then(function(response) {
			var contentType = response.headers.get("content-type");
			if (contentType && contentType.includes("application/json")) {
				return response.json();
			}
			throw new TypeError("Error: Didn't receive JSON");
		}).then(function(json) {
			console.log(json);
			self.setState({
				content: json
			});
			console.log(self.state.content)
		}).catch(function(error) {
			console.log(error);
		});
	}
	render() {
		return(
			<div className={styles.home}>
				{this.state.content.map((item) => (
					<Link to={"/" + item.id} key={item.id}>
						<Entry title={item.title} />
					</Link>
				))}
			</div>
		);
	}
}

export default HomePage;
