# LichessProject
This program converts the competition pairings obtained from the program Sevilla from JBF software to post requests towards lichess, such that the tournament can be played online.

Before using it, you should make sure that the constant path_to_csv_file in 'main.py' points to the csv file obtained from the program Sevilla.
Furthermore, make sure that for all the participants the lichess username and authorization token are registered in 'auth_tokens.json'. 
The participants can request the token from lichess at https://lichess.org/account/oauth/token/create. Make sure that during the creating of the Access Token the option 'Create, accept, decline challenges' is enabled.

In 'main.py', you can also set the time specifications by changing the constants 'clock_limit' and 'clock_increment'.

By running the program 'main.py'. The program imports the csv file containing the pairings and sends the post requests to lichess for the selected pairings and clock settings.
After this, all the participating players will find their game on their home page on lichess.
Lichess also has an option to import iframes of games into a website. A file named 'game_iframes.txt' is also created by running 'main.py' and contains all the iframe embeddings which you could copy to your website should you wish to do so.

By running the program 'fetch_game_results.py' the status of all the created games of the round are printed in the command prompt to give you a quick overview of the status of the current round.
