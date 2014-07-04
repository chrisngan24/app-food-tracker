# Setup
========

Begin by installing with Heroku
* https://devcenter.heroku.com/articles/getting-started-with-python

Set up Mongo HQ
* http://www.elliotbradbury.com/use-mongohq-heroku-without-verifying-account/
Connect to Mongo over client through:

```
mongo kahana.mongohq.com:10042/python_inc -u <user> -p <password>
```

To set Mongo HQ URL, do:
```
 heroku config:set MONGOHQ_URL="mongodb://<user>:<password>@kahana.mongohq.com:10042/python_inc"
```
