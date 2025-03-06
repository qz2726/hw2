# Django Project Setup and Testing Guide

## Local Setup

```sh
# 1. Navigate to your project directory
cd "/Users/asher/Documents/New York University/Academics/Spring 2025/Software Engineering I/Coding/homework1/ebdjango"

# 2. Activate your virtual environment
source ~/eb-virt/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Collect static files
python manage.py collectstatic --noinput

# 6. Run the development server
python manage.py runserver
```

After running the server, open **http://127.0.0.1:8000/polls/** in your browser to test your application locally.

## AWS Deployment

```sh
# 1. Navigate to your project directory
cd "/Users/asher/Documents/New York University/Academics/Spring 2025/Software Engineering I/Coding/homework1/ebdjango"

# 2. Activate your virtual environment
source ~/eb-virt/bin/activate

# 3. Set up AWS Elastic Beanstalk environment (only needed if setting up from scratch)
eb init -p python-3.12 ebdjango

# 4. Deploy the application
eb deploy

# 5. Open the AWS-hosted application in a browser
open "http://$(eb status | grep CNAME | awk '{print $2}')/polls/"
open "http://$(eb status | grep CNAME | awk '{print $2}')/admin/"

```

Your AWS-hosted Django application should now be accessible at:
```
http://django-env.eba-cc9ambe4.us-east-1.elasticbeanstalk.com/polls/
http://django-env.eba-cc9ambe4.us-east-1.elasticbeanstalk.com/admin/
```

## Debugging & Logs

```sh
# Check local logs
cat logs/debug.log

# Check AWS logs
eb logs
```

If you encounter issues, verify that all dependencies are installed, the database is migrated, and AWS credentials are correctly configured.
