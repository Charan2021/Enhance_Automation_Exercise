import json
import webbrowser
import requests
from requests_oauthlib import OAuth1Session , OAuth1 , OAuth2 , OAuth2Session

consumer_key = "400E87C7B9CE8E6F3FA27CBE718F591E"  # key provided by trademe after an application request
consumer_secret = "F9A50D7B5F3A473826A751F7B3C1757D" # secret provided by trademe after an application request

###########################
#AQUIRING TEMPORARY TOKENS#
###########################
request_token_url = 'https://secure.tmsandbox.co.nz/Oauth/RequestToken' # requesting token without user scope
#request_token_url = 'https://secure.tmsandbox.co.nz/Oauth/RequestToken?scope=MyTradeMeRead,MyTradeMeWrite,BiddingAndBuying'
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      #signature_type=consumer_secret,
                      signature_method="PLAINTEXT",
                      callback_uri="https://www.website-tm-access.co.nz/trademe-callback")
fetch_response = oauth.fetch_request_token(request_token_url)
print(fetch_response)
auth_token = fetch_response.get('oauth_token')
auth_token_secret = fetch_response.get('oauth_token_secret')
print(auth_token)
print(auth_token_secret)


#####################################
#AUTHORIZING ACCESS TO USERS ACCOUNT#
#####################################
base_authorization_url = 'https://secure.tmsandbox.co.nz/Oauth/Authorize'
authorization_url = oauth.authorization_url(base_authorization_url)
print ('Please go here and authorize,', authorization_url)
#Open Browser and enter username and password
webbrowser.open(authorization_url, new=2)


redirect_response = input('Please paste the full redirect URL here: ')
#Paste the URL

oauth_response = oauth.parse_authorization_response(redirect_response)
verifier = oauth_response.get('oauth_verifier')
print(verifier)


##################################
#ACQUIRING FINAL TOKEN AND SECRET#
##################################
access_token_url = 'https://secure.tmsandbox.co.nz/Oauth/AccessToken'
oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=auth_token,
                      signature_method="PLAINTEXT",
                      resource_owner_secret=auth_token_secret,
                      verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)
print(oauth_tokens)

oauth_token  = oauth_tokens.get('oauth_token')
print(oauth_token)
oauth_token_secret = oauth_tokens.get('oauth_token_secret')
print(oauth_token_secret)

#############
#TO GET DATA#
#############
protected_url = 'https://api.tmsandbox.co.nz/v1/Search/Motors/Used.json'
watchlist_url="https://api.tmsandbox.co.nz/v1/MyTradeMe/Watchlist/All.json"

oauth = OAuth1Session(consumer_key,
                      client_secret=consumer_secret,
                      resource_owner_key=oauth_token,
                      resource_owner_secret=oauth_token_secret,
                      signature_method='HMAC-SHA1',
                      verifier=verifier)
car_contents = oauth.get(protected_url)
var = car_contents.content
print(var)
