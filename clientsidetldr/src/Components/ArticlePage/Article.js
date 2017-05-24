import React, { Component } from 'react';

class Article extends Component {
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

export default Article;
