import React, { Component } from 'react';
import Header from './Components/Header';

class App extends Component {
  render() {
    return (
      	<div style={divStyle} className="App">
		<Header />
     	</div>
    );
  }
}

const imgUrl = "http://www.planwallpaper.com/static/images/colorful-triangles-background_yB0qTG6.jpg"

const divStyle = {
	backgroundImage: 'url(' + imgUrl + ')',
	backgroundSize: '100% 100%',
	position: 'absolute',
	width: '100%',
	height: '100%',
}

export default App;
