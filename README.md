# G’day!

This is a mini project demonstrating some of my skills in data engineering using python.

## **Skills demonstrated:**
* Requirement understanding
* Documenting ambiguous requirement to seek clarification
* Solution design documentation using flow chart diagram
* Python programming:
  * Using basic python modules such as csv, datetime
  * Advanced python libraries such as pandas, numpy
  * Distributing complex program into multiple code files 
  * Splitting solution into multiple steps using user defined functions
  * ***EXTRACTING*** data from csv file
  * Iterating through dataset – record by record
  * Hashing algorithm such as MD5
  * Operation on data structures such as concatenations, inserts, append
  * Data ***TRANFORMATIONS*** such as data type casting, string to date transformations, searching for specific text 
  * Logging events in a program
  * Using try, except to manage unhandled exceptions and terminating program
  * Joining two data frames
  * Averages, ranking, sorting, grouping
  * Selecting and filtering columns as needed
  * ***LOADING*** sets of data into multiple json files
* Testing
* Contributing to github and markdown

## **Project requirements:**

Please refer to [this link](https://github.com/cpenc/Python_data_engineering/blob/main/Data%20Engineering.png) for project requirements.

## **Assumptions and trade-offs:**

Requirements of this project are very clear. Except the following two points.
* List post codes based on fastest response. Hint (Refer columns Request date and implementation Date)
* Top Agents based on postcode and amount

I call these two points ambiguous because if you see the [input dataset](https://github.com/cpenc/Python_data_engineering/blob/main/Transaction.csv), the response times can be figured out at an account ID level. So, one could list post codes based on fastest response using several logics such as:
* Fastest *average* response time per post code
* Fastest *median* response time per post code

Similarly, top agents can be ordered in relation to fastest response post codes or just within post codes regardless of response ranking of a post code.

## Decisions I made:
So just to make things easy for myself and demonstrate similar skills only once, I have chosen to use the following logic for grouping, ranking, sorting and extraction
* Calculated average response time (implementation date minus request date) of all post codes.
* Ordered post codes in the ascending order of average response times within a post code
* Then within a post code ordered $ amount in descending order
* Did not worry about ordering agents in relation to $ amount. Because, that would require another grouping and sorting.


## **Solution design:**

Please refer to this [High level design diagram](https://github.com/cpenc/Python_data_engineering/blob/main/Design%20Diagram.PNG), if you want to understand the breakdown of steps implemented in the solution.

## **Extract files**:
Out of the 30K records in the input file, some where filtered out where data was questionable. The rules used to filter out are in the [High level design diagram](https://github.com/cpenc/Python_data_engineering/blob/main/Design%20Diagram.PNG). The rest of the records are groups and extracted 1K per json file as mentioned under the decisions I made section above. I've uploaded 10 of the 31 output files to this repo. One of the samples is [here](https://github.com/cpenc/Python_data_engineering/blob/main/extract_30.json).
