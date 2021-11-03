# Job_Search_Shortcut
Automate opening job search browser windows

This is my first python project which uses selenium webdriver to automate the opening of n number of browser **tabs**. 

the variable vacancies contains a list of URLS. 

A for loop iterates over vacancies[] by:

  - opeing up a broswer tab and loading the URL, followed by an explicit wait. 
  - Grabbing the window handle
  - Switching to the next tab, using the window handle as an argument, to the switch_to_window method
  - Using a GET request to load the URL address
  - Loop


The project in its current form is incomplete, as the initial idea is for selenium to open **browser windows**. rather than **browser tabs**, that I could track each branch of my vacancies search.

Next phases of the project 

- Using Fstring variable named search. This variable will be appended to the URLS to make the vacancies list dynamic. Current URLS are hardcoded.
- Working out the solution to the **browser windows**.
