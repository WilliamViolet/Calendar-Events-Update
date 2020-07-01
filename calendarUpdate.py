from google_auth_oauthlib.flow import InstalledAppFlow
import pickle 
import pprint

scopes = ['https://www.googleapis.com/auth/calendar']

flow = 
InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()