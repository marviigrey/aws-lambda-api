We want to create a backend API endpoint that handles HTTP using lambda function and API. This is a serverless architecture because we do not need to spin up an EC2-instance or any server to be able to carry 
out this task. 
Steps:
1. log in to the AWS management console and navigate to lambda. 
   -  create a lambda function called "apiFunction". we will be creating it from scratch so select "create from scratch". We then choose our runtime which will be Python.
   -  leave the remaining settings at default then move to create your function.
   -  After creating the function we then move to writing our code. the code in in the file called lambda.py and can be found in this repo with comments that will be used to explain each code. The code is a Lambda function that takes an incoming event, extracts a query parameter named 'slack_name' (with a default value if not provided), retrieves the current day of the week and UTC time, and constructs a JSON response with this information along with fixed values for 'track' and GitHub URLs. Finally, it returns the JSON response with a status code of 200 for success.
  
2. Next, we create an API-Gateway to integrate with our Lambda function.
   -  We navigate to the API gateway page, and create a resource called "apiFunction"
   -  create an integration with the previously created lambda function called "apiFunction",
   -  Automatically it uses the $default stage so we create routes and add HTTP requests.
   -  We create two GET routes, one for Getting the slack name and the other for getting the track name, it's all specified in the lambda code.
   -  After creating the routes we can then access our endpoint using the generated URL by API GATEWAY. you should get a response in a JSON format that shows the slackname, track name, GitHub repo, GitHub repo file, date & time, and the status code for HTTP.
