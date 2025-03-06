# Homework 2
Django Application Tutorial


## Build Status
[![Build Status](https://app.travis-ci.com/qz2726/hw2.svg?branch=main)](https://app.travis-ci.com/qz2726/hw2)


## Coverage
With &&service
[![Coverage Status](https://coveralls.io/repos/github/qz2726/hw2/badge.svg?branch=main&&service=github)](https://coveralls.io/github/qz2726/hw2?branch=main)

Without &&service
[![Coverage Status](https://coveralls.io/repos/github/qz2726/hw2/badge.svg?branch=main)](https://coveralls.io/github/qz2726/hw2?branch=main)


Without branch
[![Coverage Status](https://coveralls.io/repos/github/qz2726/hw2/badge.svg)](https://coveralls.io/github/qz2726/hw2?branch=main)


## Application URL
http://ebdjango-env.eba-bphmfimt.us-east-1.elasticbeanstalk.com/polls/



## Travis CI and Elastic Beanstalk Deployment Verification

In the `test` branch, go to:  
[ebdjango/templates/home.html](https://github.com/qz2726/hw2/blob/test/ebdjango/templates/home.html)

Change:  
```html
<h1>Welcome to the Django App!</h1>
```
to:  
```html
<h1>Hello! Welcome to the Django App!</h1>
```

Then, open a pull request from the `test` branch to the `main` branch. Click "Merge pull request".

You’ll see the Travis CI PR build start. Once the build of the main branch passes, the app gets successfully deployed to Elastic Beanstalk (EB).

You can confirm the deployment by visiting:  
[http://ebdjango-env.eba-bphmfimt.us-east-1.elasticbeanstalk.com](http://ebdjango-env.eba-bphmfimt.us-east-1.elasticbeanstalk.com)

You should now see the updated message:  
**Hello! Welcome to the Django App!**
