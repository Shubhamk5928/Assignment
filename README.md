# Assignment 
Its is an unique word counter that count the  frequency of unique words from Static Website and return the Count with their frequency in JSON Format

## problem Statement 
Write a microservice in python that takes a URL of a static website as an input and identifies all the unique words and how many times they occur on a web page. The output is a list of words in JSON format along with the frequency of occurrence (number of times the word is repeated).

My Approch is Firstly,
1) Install the required packages
2) Import it in my file
3) Then I made a function count_word() which takes the website URL
4) After I just Simply use request.get() to fetch the get request from the server
5) Then I use Beautiful Soup to parse the fetch content make it navigateful using beautifulsoup(response, html.parse)
6) then i made a two list - One for all the words 
7) second for count the word
8) then i iterate over the list using for loop having condition if word id repeated then count value id increased
9) At last I just Simply Print it in JSON Format using JSON Parser

Thanks for reading ❤️, fell free to connect
shubham kumar
