import pprint
#to output the json file which we get from google
from googleapiclient.discovery import build

def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="{API KEY}")
#q= query - replace with your choice
  res = service.cse().list(
      q='lectures',
      cx='{Search Engine ID}:kilqn8tgk9s',
    ).execute()
  pprint.pprint(res)

if __name__ == '__main__':
  main()
