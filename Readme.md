# whale-catching-tweets
# Summary 
The DA24 Hyper Island Python module called for us to extract information from Twitter into a database. This script extracts timeline tweets from the sophisticated cryptocurrency transaction reporting user 'whale_alert' and transforms them by cleaning and structuring target information into a relational database (CSV) ready for further analysis.
# Future Purpose
I note that this is a beta version with the future intent of this script to automatically run every 24 hours to have a continious stream of data that can be analysed over long periods of time. Ultimately I would like to test to see if and what extent of whale transaction events actually have an influence on a given cyrptocurrency price movement. 
# Detailed Description: Problem & Context
A feature of cryptocurrency on the blockchain is that it’s transparent and transfers are publicly stored on a distributed ledger. A group called Whale Alert has made use of this transparency to find and track so called ‘whales’ using AI. Whales are accounts which make high value transfers in the millions of dollars in a given cryptocurrency. These wallets as a whole can occupy a significant share of any cryptocurrency. Whale Alert publish these transfers automatically on various pages, including Twitter. People use these notifications as an indicator of price movement to trade and make profit. Tradable indicators could include large volumes of cryptocurrency movement into an exchange, which is a bearish (sell) indicator, whereas the opposite may be a bullish (buy) indicator as people may be accumulating and holding. It is important to understand the market conditions which may influence these transfers and this indicator should not be relied on alone but together with several other indicators.

A key problem with making use of these transfer notifications is the sheer amount of them, which can be between 30 and 50 in a day. You need the ability to make sense of them and put them into context, particularly quantitatively and historically, to understand what extent of transfers are significant. That is where this project seeks to collect and organise the key details of these transaction notifications into a database, which is ready for quantitative analysis.  
# Scope
•	Extract tweets from Twitter user @whale_alert timeline

•	Tweets extracted must be within a given full day (24 hours) with a max limit of 50 tweets

•	Only critical tweet details must be extracted and fit within this CSV column structure: ['Date', 'Amount (No.)', 'Cryptocurrency', 'Amount ($)', 'Currency', 'Action', 'From', 'To']

•	Tweets which don’t fit the desired specifications must be sent to a junk CSV file to monitor if any useful data is being lost, so the script can be adjusted to capture this information

# Data Dictionary
| **Name** | **Definition** | **Data type** | **Example values** | **Required?** |
| --- | --- | --- | --- | --- |
| Date | Date and time tweet was created at | Date & Time | 2022-12-23 22:06:26+00:00| Yes |
| Amount (No.) | The amount in number of units of the particular cryptocurrency | Integer | 4041785 | Yes |
| Cryptocurrency | The name of the cryptocurrency being transacted | Text | BTC, ETH, USDC, USDT, UNI, XRP | Yes |
| Amount ($) | Fiat currency amount attached to cryptocurrency units being transacted | Integer | 50000565| Yes |
| Currency | Specific fiat currency being used to calculate Amount ($) | Text | USD | Yes |
| Action | What specific action or operation is the transaction showing | Text | Transferred, burned, minted | Yes |
| From | Where is the transaction coming from (origin) or occurring at | Text | Jason Sun, unknown wallet, USDC Treasury | Yes |
| To | Where is the transaction going to (destination) | Text | Jason Sun, unknown wallet, USDC Treasury | No |

# Installations 
The following Python modules are used: 

•	tweepy

•	re

•	datetime

•	pandas 

•	pytz

# Usage instructions
The code is packaged inside a function that has to be called. My own personal tweepy API authorisation keys and tokens are used inside the function. Please use your own authorisation if possible as technically authorisations should not be shared. 

# Licensing information
To run the function you require Elevated Access Authorisation from Twitter's Tweepy API.

# Contact information
Feedback encouraged and welcomed to max.bindon@hyperisland.se 
