import React, { Component } from 'react';
import styles from "./EntrySortButtons.css";

class EntrySortButtons extends Component {
	constructor() {
		super();
		this.state = {
			sortOption: 0
		}
	}
	sortChange(numb) {
		this.props.changeEntryOrder(numb)

		this.setState({
			sortOption: numb
		});
	}
	render() {
		return(
			<div className={styles.sortbtnContainer}>
				<span className={styles.infosortbtn + " " + (this.state.sortOption == 1 ? styles.selected:'')} onClick={() => this.sortChange(1)}>Top Rated</span>
				<span className={styles.infosortbtn + " " + (this.state.sortOption == 2 ? styles.selected:'')} onClick={() => this.sortChange(2)}>Most Viewed</span>
				<span className={styles.infosortbtn + " " + (this.state.sortOption == 3 ? styles.selected:'')} onClick={() => this.sortChange(3)}>Most Recent</span>
			</div>
		);
	}
}

export default EntrySortButtons;
