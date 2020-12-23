# Flask MongoDB Login Example

This is an example Flask App that uses Flask-Login and MongoDB to create a Login, Logout and SignUp.

The example Flask-App uses: 
- `Flask-Login` to handle authentication
- `MongoDB` as database
- `Bcrypt` to encrypt the password.

For using this you should have a database similar to the following. _Copy the below code for easy use_ :
```
{
        "_id" : ObjectId("5fc77cf80c549d947d6b9abb"),
        "name" : "Admin",
        "username" : "admin",
        "password" : BinData(0,"JDJiJDEyJFF3bWJQbVJjN3h2UzI1UTJicUcwaS5NSXV5LmlCNVN0RVpwT3NxQ1BDZ1dyWE9GeDU3LnBT"),
        "admin" : true
}
{
        "_id" : ObjectId("5fc8fb990f7101bd1c85b45a"),
        "name" : "Sample User",
        "username" : "sampleuser",
        "password" : BinData(0,"JDJiJDEyJEZTdW1mblB4dEwyYTZ6clRBaFNHRy5nL0lzZjEuZ2hVYWZhN3A3S3BnZzFTUEx1Qi50Q3B1"),
        "admin" : false
}
```
 In the above code the credentials of Admin User are :
```
username : admin
password : admin1234
```

## Routes
The routes can be configured as **all users**, **registered users only** or **admin only**.  
The new user is defaulted to **`admin : false`**, to give admin previlages to a user change the above mentioned line of code to  **`admin : true`** manually in the database.  
Routes for the example Flask-App are :
- `/` 
- `/auth/login` 
- `/auth/signup`
- `/auth/protected-route`
    - This route can only be accessed after login.
- `/auth/admin-panel`
  - This route can only be accessed after loging in as `admin`.
  - You can use admin route to `delete users` and `reset password`.
  - NB: _You need atleast One admin user to access the `/auth/admin-panel` route_
## Screenshots
![](static/assets/picasa.png)