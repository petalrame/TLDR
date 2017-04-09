import React, { Component } from 'react';

class Article extends Component {
	constructor() {
		super();
		this.state = {
			imgsrc: "https://i.ytimg.com/vi/tntOCGkgt98/maxresdefault.jpg"
		}
	}

	render() {
		return(
			<div style={divStyle}>
				<h3>Article Title</h3>
				<img style={imgStyle} src={this.state.imgsrc} />
				<p>Article Content</p>
			</div>
		);
	}
}

const divStyle = {
	backgroundColor: 'rgba(129, 158, 201, 0.4)', 
	color: 'grey',
	textAlign: 'center',
	padding: 10,
	width: '80%',
	margin: '0 auto'
}

const imgStyle = {
	width: 400,
	height: 300,
	opacity: 0.8,
	verticalAlign: 'left'
}

export default Article;
