




# stmortem Report

## Incident report - 504 Error while accessing a given URL
 
### Issue Summary
Between 23:00 hrs and 23:39 hrs of August 09 2023, my Apache2 server was down. This was caused by a mistyped file name in the ‘.ini’ settings of the apache2 server configuration file. This led to premature closing of the apache2 server thereby resulting in 504 errors whenever I try accessing a website.

### Timeline

- 23:00 - 500 error is displayed when I try accessing a website
- 23:05 - I checked to ensure Apache and MySQL are up and running.
- 23:05 - Check revealed that the server was working properly.
- 23:10 - I did a quick restart of Apache2 server and it returned status quo - 200
- 23:12 - Curling a website returns OK
- 23:26 - I checked /var/log to see if the Apache2 server was shutting down for whatever reason. Surprisingly, there was no error log. 
- 23:32 - I checked the ‘.ini’ settings to know the status of the error log, I found out it was turned off
- 23:25 - I  turned on the error logging and  restarted the apache2 server. 
- 23:27 - I accessed the error logs again, and this time it was there.
- 23:29 - I Reviewed the error logs and discovered a mistyped file name which led to an incorrect loading, leading to a premature closing of the apache2.
- 23:35 - I fixed the filename and restarted the Apache2 server.
- 23:39 - Server is now running and the website is loading.


### Root Cause and Resolution

The issue was as a result of an incorrectly named essential configuration file in the ‘.ini’ setting of the server's configuration. This led to the file not being read by the system whenever the server initializes or starts. As a result, it halts the file’s function and fails to display log errors, thereby having the server return a 500 Error wherever it is curled.

On the discovery that no error log file was being created for the errors, the ‘all error logging’ was turned and the error logging the apache server was restarted to check if any errors were being registered in the log. Only then it was discovered that a file with a .php extension was not found in the wp-settings.php file. This was as a result of the incorrectly spelled file name in the .ini settings. 

An easy fix was achieved by spelling correctly, the file  name and effecting the change. Afterwards, a restart or initialisation restores the server's expected response whenever it is curled. 



### Corrective and Preventive Measures

- All servers and sites should have error logging turned on for proper identification of errors and bugs.
- All servers and sites should be tested locally before deployment in other to minimize time spent on fixing
