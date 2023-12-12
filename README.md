# Project 2 Write-Up

## Data Ingestion and Analysis

### Process
I wrote my code in a Jupyter Notebook so that I could execute blocks of code separately. This was useful when it came down to writing code for analysis
so I could run the cells for the analysis with the already-created database without starting the whole process over. I decided to use a MySQL database
because that was what I was most comfortable using already. The methods for getting and creating tables were reused from class and I used localhost.
The method of scheduling the API call and retrieval was done using Python's schedule library. This worked by setting a function to be executed by the
schedule every minute at :00 seconds 60 times. At each interval, the function would make an API call to the URL, append the three variables from the JSON
to a dataframe, and increment a count variable to keep track of which iteration the system was at. Once all 60 iterations were performed, the schedule
would no longer run every minute and the newly created dataframe of 60 rows was then added as a table to a database.

### Analysis
The code would query the database to start and create a pandas dataframe. The first analysis I did was graphing both Factor and Pi over Time and viewing
the shape. I also would perform basic math analysis using df.describe() and .info(). My first impressions were that the Factor variable grew at a quadratic
rate and that Pi oscillated towards a single point of convergence. When I view the tail end of the data, however, it was clear that they did not relate to
the data directly previous of them. This makes sense as I believe that the data resets at the beginning of every hour and considering I started collecting the 
data at :05 minutes, the five data points at the end would then belong at the beginning. Placing them at the beginning would continue to support my initial
hypotheses.

Looking at the individual data points for Factor, I believe that the quadratic relation is cubic. This is because the first points proceed as follows: 1, 1,
8, 27, 64 which follow x^3 for x = {0, 1, 2, 3, 4}. To confirm this, I fit the data using a cubic regression model. The resulting graph looked as aligned as
it could be. I then calculated the R^2 value to see how well the cubic function fit the data and found that it had a perfect R^2 value within four decimal 
points of 1.0000. This confirms that it is a cubic function.

For Pi, the name seemed to obviously imply that the number trying to be reached is Pi. The mean of all the data of Pi is 3.168573 and the final pint at 59
minutes was 3.1415975, both of which were very close to pi. The final point would be the closest to Pi if my guess is correct. The Error of the final point
using pi is 1.54986578E-6 which is very small and the error it began with was 0.27323 for a value of 4.0.

Overall, the value of Factor is growing at a cubic rate, and the value of Pi approaches the actual value of pi as time goes to infinity (up to when hour ends
at it restarts of course). One thing to note as well is that it appears that the factor may be related to pi as it approaches its real value. For the first two
minutes of the hour when Factor is equal to 1, Pi remains the same at 4.0. This seems to suggest that perhaps Pi is estimated using Factor or they are calculated
by related means. This did not seem testable, however, but was something of interest.
