# Real-estate-consultancy

The dataframe in possession includes information about houses and rooms offered on the platform operating in the field of the gig economy "Airbnb" in the city of New York. 
Inside it there are several columns containing different categories of information (ex: host, neighbourhood, availability, coordinates...). 

In Windows 10 environment, using as an interpreter the IDE JetBrains PyCharm CE 2019.2.2 and as a tool for creating a MySQL Workbench 8.0 CE database  I analyzed the dataframe creating an analysis path reasoning from the point of view ofthe advice to be given to an agency eager to insert some of its apartments on  Airbnb.

In the first step, using the Pandas library, I divided the dataframe by districts (i.e.  neighbourhood_group) and for each of them I selected the Entire home/apartment. After this extrapolation I looked for the average price for each of the districts deciding to enter the final results in a histogram in order to have a fast and intuitive graphic display on which band can be more interesting for a series of apartments to be put to income.

The band chosen is that between 150 and 175 while the most interesting district for which the final decision will most likely preponderà (given the high tourist attractiveness) is that of Manhattan.![Senza titolo](https://user-images.githubusercontent.com/63848150/188696719-a75d97a7-6c29-4f8d-a5f0-3f2dd9eef601.png)

To verify if the choice of Manhattan was far-sighted, I choose to carry out an analysis creating a comparison with the second most expensive district: Brooklyn.

In the second step, therefore, I first use a trigonometric formula, using the Numpy library, which allows you to convert the latitude and longitude parameters into km. 
Subsequently, two points of reference for each district were established,  capable of creating attractiveness for the agency: The Brooklyn Bridge and Wall Street. 
Through these two landmarks I create a constraint: the apartments found using these parameters must fall within a radius of up to 2km from the reference point. 
In addition, to deepen the market research, the analysis was performed by dividing the price range into additional mini-ranges so that the  choice to invest in Manhattan could be  more accurately approached.

In this case the pie-chart proves to be the most immediate graph to interpret the distribution of the apartments in the mini-intervals with the constraints described above.
<img width="322" alt="Schermata 2022-09-06 alle 19 01 51" src="https://user-images.githubusercontent.com/63848150/188696761-7d4a1030-9e65-4eda-b3e6-8362cb2a9935.png">
<img width="314" alt="Schermata 2022-09-06 alle 19 02 00" src="https://user-images.githubusercontent.com/63848150/188696833-aad7abbc-0287-4851-8863-43a7cf0e050b.png">

You can notice how in the slice 155-160 the percentages are very similar, and since the number of apartments in the district of Manhattan è much higher, we consider the lattero (especially in the area of Wall Street) the more interesting (and interested)o) from a market point of view.

Once the slice of the market in which the agency may have a particular interest in entering, the last analysis involves the knowledge of competitors and therefore of the owners of apartments in that same slice.

As a third step, therefore, the selection  implements two other categories of data in particular: 
the number of reviews and the date of last review. 

The two categories reveal, especially if combined together, the industriousness in the area, in quantitative terms related to a chronological period.

The two categories of data have been elaborated, placing the amount of reviews in a decreasing way and finally taking only the first 10 of the list, in order to directly have the reference competitors in the area.
![Senza titolo2](https://user-images.githubusercontent.com/63848150/188696899-252e13a9-0599-4fbf-8d0f-56d9da3bc107.png)

The resulting graph places on the Y axis the amount of reviews per apartment, while on the X axis it places the dates relating to the latest reviews written by users. This bar-chart can be used bythe agency as the dominant level of industriousness  in that particular portion of the market, so that you can get an idea of the pace of work that it will have to sustain if it wants to keep its offers competitive.

Within the processing I also entered other categories of data, so as to have a portion (constrained) of dataframe with inside: number of reviews, last review, latitude, longitude, name of the owner.

These categories of data are sufficient to create a map representing the area of interest with a marker for each apartment analyzed. 
To facilitate its visualization, the map (saved in html format within the directory containing the various analyzes) is interactive.
<img width="319" alt="Senza titolo3" src="https://user-images.githubusercontent.com/63848150/188697083-f3d4ccf2-22b6-486c-b7d2-f8c6f2f7f77d.png">

These categories of data are sufficient to create a map representing the area of interest with a marker for each apartment analyzed. 
To facilitate its visualization, the map (saved in html format within the directory containing the various analyzes) is interactive.Once the interpreter has been started:
 - click on "create new project"
 - unzip the rar file  within the created directory
 - install the required modules in the project (eg.  pandas) by going to: 
file > settings > project > project interpreter > use the + symbol at the top right > search for modules and install them

To launch the script you need to run the  first analysis, then the second and ![Uploading Senza titolo.png…]()
finally the third (to get the data in the database table you will need to replace the parameters of MySQL connections with your own).

PS: I inserted both the original files in .py format and the files in jupyter notebook. The latter have the comment to the code in English.
