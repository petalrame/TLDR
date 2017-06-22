import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';

import PoliticsPage from './Pages/PoliticsPage/PoliticsPage';
import TechPage from './Pages/TechPage/TechPage';
import FashionPage from './Pages/FashionPage/FashionPage';
import CrimePage from './Pages/CrimePage/CrimePage';
import EconomyPage from './Pages/EconomyPage/EconomyPage';
import SportsPage from './Pages/SportsPage/SportsPage';
import HealthPage from './Pages/HealthPage/HealthPage';
import HomePage from './Pages/HomePage/HomePage';
import ArticlePage from './Pages/ArticlePage/Article';

const politicsControl = () => (
	<Switch>
		<Route exact path="/politics" component={PoliticsPage} />
		<Route path="/politics/:number" render={() => <ArticlePage />} />
	</Switch>
)

const economyControl = () => (
	<Switch>
		<Route exact path="/economy" component={EconomyPage} />
		<Route path="/economy/:number" render={() => <ArticlePage />} />
	</Switch>
)

const techControl = () => (
	<Switch>
		<Route exact path="/tech" component={TechPage} />
		<Route path="/tech/:number" render={() => <ArticlePage />} />
	</Switch>
)

const sportsControl = () => (
	<Switch>
		<Route exact path="/sports" component={SportsPage} />
		<Route path="/sports/:number" render={() => <ArticlePage />} />
	</Switch>
)

const fashionControl = () => (
	<Switch>
		<Route exact path="/fashion" component={FashionPage} />
		<Route path="/fashion/:number" render={() => <ArticlePage />} />
	</Switch>
)

const crimeControl = () => (
	<Switch>
		<Route exact path="/crime" component={CrimePage} />
		<Route path="/crime/:number" render={() => <ArticlePage />} />
	</Switch>
)

const healthControl = () => (
	<Switch>
		<Route exact path="/health" component={HealthPage} />
		<Route path="/health/:number" render={() => <ArticlePage />} />
	</Switch>
)

const homeControl = () => (
	<Switch>
		<Route exact path="/" component={HomePage} />
		<Route path="/:number" render={() => <ArticlePage />} />
	</Switch>
)


class Index extends Component {
	render() {
		return(
			<div>
				<Switch>
					<Route path="/politics" component={politicsControl} />
					<Route path="/economy" component={economyControl} />
					<Route path="/tech" component={techControl} />
					<Route path="/sports" component={sportsControl} />
					<Route path="/fashion" component={fashionControl} />
					<Route path="/crime" component={crimeControl} />
					<Route path="/health" component={healthControl} />
					<Route path="/" component={homeControl} />
				</Switch>
			</div>

		);
	}
}

export default Index;
