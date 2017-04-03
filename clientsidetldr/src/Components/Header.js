import React, { Component } from 'react';

class Header extends Component {
	render() {
		return (
			<div style={divStyle}>
				<h1>TLDR</h1>
			</div>
		);
	}
}

const divStyle = {
	backgroundColor: 'grey'
}

export default Header;
