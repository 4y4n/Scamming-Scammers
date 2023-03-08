## Scamming-Scammers
Simple script made to attack phishing websites

I was approached on Instagram with a link to vote for someone at an influencer program. It was just a low budget instagram login page that was clearly made to steal someone's account information.

So I made this simple python script that posts generated usernames and passwords to their server.

# To use:
1. Inspect the web page which you are trying to input information to
2. Find the <form> tag and take input the action url into the url variable
3. Find the <input> tags that are associated with the username and password fields and input the name string into the inUser and inPass variables
4. Run the program and let it burn their servers to the ground!