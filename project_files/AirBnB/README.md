
### 1 Business Understanding/Data Understanding
          AirBnB is an online marketplace for vacation/temporary houseing rentals.  Thier members/hosts own the property and rent via the  AirBnB marketplace.
          
          The data provides was provided each from Seattle and Bostom
          * listing.csv
          * calendar.csv
          * reviews.csv
          
          How to best position your property to make the most revenue?
          1) What property attributes correlate with higher rental prices?
          2) Which neighborhoods the best neighborhoods for price?
          3) When is the best time of year to rent?

          
          
### 2 Data Preparation
        1) Imported listing and calendar
        #clean_cal() and clean_listing()
        2) Corrected and adjusted datatypes  
        3) Took some columns and made them into booleans (presnence or absence of awnser)
        4) One Hot encoded columns that contained lists of atttributes
        
     
     
#### 3 Cleaning Data
        prep_cal()
        Price is our response variable
        1) removed all rows where price was NA
        2) Removed a column that was mostly NAs
        3) removed a few rows of the remaining NA
        
        
### 4 Modeling
        1) normailized and standardized various features
        2) Started with a LinearModel but got a very negative r^2
        3) Fit a PCA model and transformed data
            


### 5 Evaluation
        1) Used the linear model fit pca data to identify which of the attributes are more influential to price.
            Used transformed data to fit a linear model (much better r^2 approx 0.3)
            Used coefficents from linear model along with the pca feature weights to identify 
            common attributes that are coorelated with higher prices
        2) Also simply looked at highest coorelation between components and price.
            Confirmed what PCA model identified
        3) Created graphs to evaluate the price differences of the identified attributes.
        4) Created graphs to evaluate the price differences between neighboorhoods
        5) Created graphs to evaluate the price differences throught he year.
### 0.3.5 Deployment
        1) Created a blog (draft) with the results via Medium - https://medium.com/@thomas.m.canty/before-you-post-to-host-64415587044a
