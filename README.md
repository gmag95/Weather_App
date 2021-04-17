# Weather App

This widget shows the most relevant weather informations about a specific region of the United States, based on the ZIP code written by the user in the entry box. The data is pulled in real time using the Airnow.gov API.

Three parameters are shown by the widget:
* Ozone: the level of ground-level ozone, an harmful air pollutant
* PM 10: coarse particles with a diameter of 10 micrometers or less
* PM 2.5: fine particles with a diameter of 2.5 micrometers or less

For all three parameters a lower value equals less air pollution

The background color of the widget reflects the air quality index, an aggregated measure of air quality measured as the highest of the three parameters previously illustrated:

* Green: air quality is satisfactory
* Yellow: air quality is acceptable
* Orange: unhealty for sensitive groups
* Red: some members of the general public may experience health effects
* Purple: the risk of health effects is increased for everyone
* Maroon: health warning of emergency conditions

This is an example based on the New York City area:

![Image example](https://github.com/gmag95/Weather_App/blob/master/example_image/Weather_app.PNG)