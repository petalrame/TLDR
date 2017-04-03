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
	color: 'grey',
	textAlign: 'center',
	padding: 10
}

const imgStyle = {
	width: 400,
	height:300,
	opacity: 0.8,
	inlineBlock: 'left'
}

export default Article;
