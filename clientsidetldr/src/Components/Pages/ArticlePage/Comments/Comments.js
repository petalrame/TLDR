import React, { Component } from 'react';

class Comments extends Component  {
	render() {
		return(
			<form>
				<input placeholder="Enter Text"></input>
				<input type="submit" value="submit"></input>
			</form>
		);
	}
}

export default Comments;
