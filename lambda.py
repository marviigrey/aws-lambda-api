import json
import datetime

def lambda_handler(event, context):
    # Extract query parameters from the event
    # We're looking for a query parameter named 'slack_name' in the request.
    # If it's not present, we default to 'Ezemba Marvellous'.
    slack_name = event.get('queryStringParameters', {}).get('slack_name', 'Ezemba Marvellous')
    
    # Get the current day of the week
    # We're using Python's datetime library to get the current day of the week.
    current_day = datetime.datetime.now().strftime('%A')
    
    # Get the current UTC time
    # We're using Python's datetime library to get the current UTC time in a specific format.
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Define other required information
    # We're setting some fixed values for 'track' and GitHub URLs.
    track = "backend"
    github_file_url = "https://github.com/marviigrey/HNG-BACKEND-INTERNSHIP/stage1/app.py"
    github_repo_url = "https://github.com/marviigrey/HNG-BACKEND-INTERNSHIP/stage1"

    # Prepare the JSON response
    # We're creating a dictionary called 'response' that contains all the information we want to return in the response.
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/marviigrey/HNG-BACKEND-INTERNSHIP/stage1/app.py",
        "github_repo_url": "https://github.com/marviigrey/HNG-BACKEND-INTERNSHIP/stage1",
        
        "status_code": 200  # Setting the HTTP status code to 200 for success.
    }
    
    # Return the response in the required format
    # We're returning a dictionary containing 'statusCode' and 'body', where 'body' is a JSON-serialized version of our 'response' dictionary.
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
