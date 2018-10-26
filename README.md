# Codefundoo_Project : Alarming System Model For Earthquake Damage Prevention 
## TEAM                   THE BLACK PEARL 
###                       Captain Kumar Harsh, First Mate Siddharth Singh Chauhan
In rural India, and even in urban areas, people are unaware of the upcoming disasters. Suppossing a family sleeps at ten in the night, and at twelve, an earthquakre hits in a nearby state and it is coming for them, how are they to know? Surely, nobody sleeps with the news on, and we doubt that would help. Also, most people that are affected in such natural disasters are often uninformed, for the news is always covering the events that led to the disaster and the aftermath and not where it might hit next. Regarding this practical concern, the affected population has hardly any prior information. Not to mention the people who drive. Most prefer to play their own songs than the radio. Who knows if they are driving straight into their oblivion?

It is a scientific **impossiblity** to **predict** earthquakes. In the words of USGS: 
>Can you predict earthquakes?
>No. Neither the USGS nor any other scientists have ever predicted a major earthquake. We do not know how, and we do not expect to know how any time in the foreseeable future.

That is why we propose an algorithm, that can scrape data from all sorts of government websites, media, from facebook to news websites, and apply geostatistical analysis along sentiment analysis of the public sentiment to rate the imminence of the danger according to the location of the deployment of our program. We further plan to use this sentiment, along with other geo-statistical data (like the distance of the epicentre of the quake or focal point of the flood from the place our algorithm is calculating from), fed into a neural network in a multiclass classifer that predicts the threat levels ('Negligible', 'Mild', 'Serious) and notfies the user that it may hit soon (display the expected collision time, etc). This algorithm can then be used together with a hardwired circuit to produce actual sirens and alarms where it might be necessary (like homes, and schools, or other public places). If it is engineered right, we believe it can save many lives.


UPDATE:
Due to lack of time and resources, much to our deepest regrets, we were unable to build web scrapers to scrape sentiment data. As such, our model still can be improved. However, we have still obtained satisfactory results just by geostatistical data analysis.

An Earthquake's aftershock speed cannot be determined with accuracy. As such it is impossible to calculate the time by which it would location B given that it has already struck A with any practical accuracy. However, we plan a future update to calculate the time duration before a flood hits due to an earthquake in a fault near the sea, as a tsunami wave's speed can be calculated. Our algorithm would find such earthquakes that occur near seas, and predict if a tsunami wave is going to hit, and if so, in what time. 
