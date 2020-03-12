Notes

Timeline
Weds
 * 3:29pm: Cloned repo fork
 * 3:48pm: Hit error trying to migrate db with `alembic upgrade head`
 * 4:35pm: Finished debugging mysql version / sqlalchemy / alembic issue: auth_plugin hack. 
    Hit pause since it took much longer than expected to just get through setup

Thurs
 * 1:52pm: restart 
 * 1:57pm: open PR
 * 1:59pm: start Task #1
 * 2:15pm: start Task #2
 * 2:39pm: start Task #3
 * 3:07pm: getting hung up on how to create a direct connection to the db to be able to execute raw SQL
 * 3:35pm: temporarily give up on using raw SQL and use the ORM instead
 * 3:56pm: Task #3 mostly complete
 * 4:03pm: finally figured out how to get a connection to the db to execute SQL
 * 4:05pm: start Task #4
 * 4:22pm: finish Task #4, and task #5 (to the extent that I wrote some regression tests before the refactoring)

## Setup ##
1. ~~Setup for a new python project as normal, we recommend using virtualenv and python 2.7~~
    * For more details, follow: http://timsherratt.org/digital-heritage-handbook/docs/python-pip-virtualenv/
1. ~~Setup a MySQL database~~
    * called ohm_assessment

1. ~~Fork the ohm_assessment repository into your own repo~~
1. ~~Set your python path, eg export PYTHONPATH=/path/to/my/repo~~
1. ~~Add the pip modules: pip install -r requirements.txt~~
1. ~~Copy config/my_development.cnf.sample to config/my_development.cnf and update with your MySQL information~~
1. ~~Create your MySQL database (use db name found in sample config file)~~
    * hm, didn't I do this in step #2? I had named it ohm_assessment anyway
1. ~~Add to your environment: FLASK_ENVIRONMENT=development~~
1. ~~Import the seed.sql file into the database~~
    * side note: uh-oh, looks like this dump was created from MySQL 5.6. I have MySQL 8.x. Hopefully that doesn't cause problems....
1. ~~Migrate to the latest version of the database with alembic upgrade head.~~
    * Error: `sqlalchemy.exc.NotSupportedError: (mysql.connector.errors.NotSupportedError) Authentication plugin 'caching_sha2_password' is not supported (Background on this error at: http://sqlalche.me/e/tw8g)"`
   * Looks like this is probably from mismatched MySQL versions :( :(.
   * Trying to get mysql to use the old auth plugin "mysql_native_password" instead of caching_sha2_password ...
   * Couldn't find a place to configure this - stackoverflow suggestions not working
   * Final workaround: hack installed version of sqlalchemy to pass a auth_plugin="mysql_native_password" flag.
        line 437: ..../ohm_assessment/ohm_venv/lib/python2.7/site-packages/sqlalchemy/engine/default.py
1. ~~Create testing environment: create config/my_test.cnf, setup a test db (using naming convention of development db but that clearly indicates this is your test db), import seed.sql, update new db:FLASK_ENVIRONMENT=test alembic upgrade head~~
1. ~~Do not commit either of your config files to the git repo.~~
1. ~~Push your changes. Note this should be on your forked repo, either on a master branch or any other branch. It should not be on the ohm_assessment repo.~~
1. ~~Open a pull request from your_repo/ohm_assessment/your_branch to ohmconnect/ohm_assessment/master.~~


### Checkpoint ###
1. ~~Before proceeding further, ensure that you can:~~
    * ~~see 3 rows in the user table in your database~~
    * ~~Start the app with `python app_test.py`~~
    * ~~The page at /dashboard is now visible and welcomes you to the task. This page will automatically log you in as user 1.~~
    * ~~You can run unit tests with `py.test tests` and see 2 tests passing.~~

## Your Tasks ##
1. ~~In the top right corner of the page, you can see the user's status level and name.  Change these to be the user's current number of points and email address.~~
    * Instead of "Status Level: <status_level> Chuck Norris", it should show the "Points: <points_value> <user_email>""

2. ~~Write a migration to do the following:~~
    * Increase the point_balance for user 1 to 5000
    * Add a location for user 2, assuming they live in the USA
    * Change the tier for user 3 to Silver

3. Add a new route at /community
    * ~~Add this as a dropdown option in the top right corner of the page, below "Dashboard"~~
    * ~~List the 5 most recent users (most recently signed up user first), with columns for user's display_name, tier, and point_balance.~~
    * ~~Assume we want this page to be fast, so use a raw MySQL query rather than any built-in ORM methods and consider what else can be done to increase page performance.~~ 
    * ~~This table of users should be bordered and striped (ie alternate rows and with grey and white stripes)~~
    * ~~Your new page likely shares some styles with the dashboard. Ensure that these styles are located in a reasonable location and without duplication.~~
    
    * OPTIONAL: Display user phone numbers in an additional column. If users have multiple phone numbers, Some users may have more than 1 phone number, each phone number should be displayed on a separate line.
    
4. ~~Refactor the User.is_below_tier method~~

5. ~~Testing~~
    * Add any unit tests that you think would be valuable. Feel free to expand existing unit tests provided in the assessment if you think they are insufficient.
    * Note: I'd write more tests, but it looks like I've run out of time.

6. Refer to the steps in "Setup" to fork and open a pull request. Note that your proficiency with Git is part of the assessment.
    * Do not be concerned if your pull request is DECLINED. We do this routinely as part of assessment for all candidates.

** BONUS: If you have not yet spent much more than two hours on this assignment, add an additional feature of your own design!
For example, what other information might be useful to see? Be creative!