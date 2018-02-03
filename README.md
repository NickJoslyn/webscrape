# webscrape
Webscrape for NCAA Data

Utilize a two-step process.
1) Scrape the names/url information of schools for relevant year and division
2) Use items from (1) to feed URL pings for this step. Extract statistical data.

The layout utilizes a main program. The main program calls the functions for both steps at appropriate times. The functions live in the relevant file for their purpose.

NCAA's websites are almost identical. Occasionally, the HTML for a specific page is slightly different than the standard. As a result, try-except error handling is included. When an error is found, the dataframe for that website is listed as empty. Since there are few exceptions to the general HTML format, this will only result in manually entering a couple data points.

Currently, the program is functional. Optimizations regarding numpy/dataframe utilization are expected. Also, error handling could be improved.
