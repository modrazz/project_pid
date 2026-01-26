# PROJECT: Optimising Advertisement Placement in Prague Public Transport 

A data analysis project using Prague Integrated Transport (PID) open data to identify optimal public transport stops and routes for advertisement placement.  

## Motivation
The purpose of an ad is to sell a product to as many people as possible. That is why placing advertisements in public transportation is a great idea since it is used daily by hundreds of people. However, not all stops or routes provide the same exposure. Thus, this project aims to analyse the Prague Integrated Transport (PID) data to identify the most effective locations for advertising placement, while also considering factors such as route type and accessibility to support more targeted campaigns.

## Sources
The analysis is based on publicly available open data from PID, available at https://pid.cz/en/opendata/, including stops, routes, service frequency and accessibility features. For the analysis, we used datasets:
- routes.txt
- stops.txt
- trips.txt
- stop_times.txt

## How to run
In your terminal, run the following command, which installs necessary libraries.
```text
pip install -r requirements.txt
```
Then simply open the project_final.ipynb file and click the 'Run All' option.

## Methodology
For the finding the optimal placement, we decided on four criteria on which we based our analysis:
- highest visibility: that is, the number of trips per stop
- longest exposure: that is, the length of a route in terms of both minutes and number of stops
- highest repetition: that is, the number of trips per route
- highly-visited locations: that is, stops located in the inner city, or near some important places, such as touristic landmarks, main train and bus station, and the airport, as well as routes that connect such stops

For the highly-visited locations, we first needed to decide which places to include. For the inner city, we chose Staroměstské náměstí and defined the area within 3 km as part of it. 

For the other criteria, we decided on the following landmarks: Staroměstské náměstí, the Astronomical Clock, Karlův most, Pražský hrad, Katedrála sv. Víta, Kostel sv. Mikuláše, Jewish quarter, Statue of St. Václav, Powder Tower, Petřín Tower, Kampa, National Theatre, Dancing House, Vyšehrad, the main train station, bus station at Florence, and the airport. For these locations, we decided to include stops within 500 meters. 

Since we thought that some of our criteria were not comparable, we settled on dividing the analysis into finding the best stops for placing an advertisement and the best routes. 

### 1. Best stop analysis
We used the criteria of high visibility and whether the stop is located in a highly-visited location, and weighted these two criteria in the following equation:

$Best.stop = w_1 \cdot visibility + w_2 \cdot location$

where we settled on $w_1 = 0.8$ and $w_2 = 0.2$. 

To analyse it further, we decided to divide the results by the type of route the stop is on. That is, we ranked the available forms of public transportation. The ranking is as follows:
1. metro
2. tram
3. bus or trolley
4. train
5. ferry

Then, for each stop, we find the highest-ranked transportation form available at that stop. For example, for the stop I.P. Pavlova, there are metro, tram, and bus stops with the same name; thus, since the metro is the highest-ranked form there, we categorised I.P. Pavlova as a metro station. Another example: Nádraží Hostivař has both tram and bus stops, but since the tram outranks the bus, we have categorised it as a tram stop.

### 2. Best route analysis
For this part, we used the criteria of longest exposure (both by time and number of stops, as two sub-criteria), high repetition, and routes connecting highly visited stops. For computing the final score, we used the following equation:

$Best.route = w_1 \cdot duration + w_2 \cdot length + w_3 \cdot location - w_4 \cdot repetition$

where we settled on $w_1 = 0.4$, $w_2 = 0.35$, $w_3 = 0.1$, and $w_4 = 0.15$.

We decided to exclude high-repetition trips, reasoning that placing ads on as many trips as possible would be costly, but that otherwise there is a high risk a passenger would take a trip without an ad.

Furthermore, we decided to exclude regional routes from our analysis, as we thought it better to focus solely on the transportation within Prague. 
Additionally, we noticed that the analysis with the current criteria was dominated by nightly services and routes operated by buses; thus, for further analysis, we decided to exclude them. 

## Key findings:
### 1. Best stops
- Top 5 stops: Smíchovské náměstí, Anděl, Želivského, Karlovo náměstí, Florenc

Since most stops in the top 20 are metro stops, with only Na Knížecí (number 12), Lihovar (number 15) and Palackého náměstí (number 16) not having a metro station, we further looked at only metro stops, only tram stops, and only bus or trolley stops. 
- Top 5 tram stops: Na knížecí, Lihovar, Palackého náměstí, Strossmayerovo náměstí, and Národní divadlo
- Top 5 bus or trolley stops: Nemocnice Krč, U hangáru, Černínova, Lukášova, and Terminál 1

### 2. Best routes
- Top 5 routes: 910, 911, 95, 908, 913

The top routes in our analysis are dominated by nightly routes (15 out of the top 20), mostly due to our criteria for long route duration and the number of stops. Thus, we decided to exclude nightly routes and see how that affects the results.

Furthermore, if not excluded, regional routes would dominate the results; we therefore excluded them before computing the best routes.

- Top 5 routes (not including nightly routes): 136, 10, 7, 12, 26

When excluding the nightly routes, trams appear to outperform bus routes, with 7 of the top 10 non-nightly routes being trams. 
- Top 5 tram routes: 10, 7, 12, 26, 22
- Top 5 bus routes:  136, 166, 201, 175, 154



## Authors
This project was created as part of a university course.
Authors: Peter Michal, Václava Sedláková
