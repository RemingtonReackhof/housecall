Alpha Special Instructions


1. Install the necessary libraries:
   1. Pip: https://pypi.python.org/pypi/pip
      1. Install this first because it will make installing the remaining packages easier.
   1. MySQL: https://dev.mysql.com/downloads/
   2. Flask: http://flask.pocoo.org/  (% pip install flask)
      1. RESTful API: http://flask-restful-cn.readthedocs.io/en/0.3.5/
      2. flask-MySql (% pip install flask-mysql)
      3. Flask-mysqldb (% pip install flask-mysqldb)
   1. Polymer: https://www.polymer-project.org/1.0/docs/tools/polymer-cli
      1. Only follow the above instructions under “Install”
1. Set-up the MySQL Database
   1. Start MySQL in System Preferences
   2. Navigate to MySQL (Run command: cd ../../usr/local/mysql/bin)
   3. Run command: ./mysql -u root -p
      1. Your username and password must both be root
   1. Run SQL in file sql/tbl_create.sql (sql> source ../../tbl_create.sql)
1. Run the program in the drteleporter folder by running (% python app.py)
2. Navigate to http://localhost:3000 in the Chrome browser. It is the only browser we are supporting at this time.
3. Click “Sign Up!” to create an account and Enjoy!