# Enhance_Automation_Exercise
1. Package requirements:
  selenium
  behave
  json
  webbrowser
  requests
  requests_oauthlib
  logging  
2. For the oauth code's consumer_key and consumer_secrete follow steps in "https://developer.trademe.co.nz/api-overview/authorisation/"  
3. To run feature scenarios use the command "behave {/pathof the feature file}

Questoin 1: 
The code first opens the tradme sanbox webpage in the given browser. Then the code uses webdriver and Select's select visible text method to select "cars,bikes&boats form static drop-down. From there , after the page loads used cars hyper link is clicked. Since the question has an open option of choosing any car, I have written my code to select the first enrty from the used cars listing( if no used cars are listed , valid error message will be printed). After that, the cars details are retrived using appropriate xpath. Happy to add code to query for a specific car model if needed.

Question 2:
A GET request is made to the list of charities end point using the URl from the tademe sandbox api document. Using request's response method the content is obtaind and encoded to string using "text()" method. Since list of elements were returned, using for loop each element is parsed to get the charity name and asserted for "St Johns".

Sorry, Questoin 3 is answered partially because:
Unable to access car details informaiton using the API url "'https://api.tmsandbox.co.nz/v1/Search/Motors/Used.json'" . Added code for 0auth in file "oauth_trademe.py".However myoauth code works fine for watchlist_url="https://api.tmsandbox.co.nz/v1/MyTradeMe/Watchlist/All.json" . To validate my code's logic kindly used the watch_list url.

consumer_key = "E93DEA683F62BA2C03C4E24DBD459490"  
consumer_secret = "13BA2DA42558960F8EB775A92B7BF6F7"

