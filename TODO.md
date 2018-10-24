Fix URLs:
---------------
Page not found (404)
Request Method: 	GET
Request URL: 	http://127.0.0.1:8000/accounts/login/

Using the URLconf defined in newsmag_project.urls, Django tried these URL patterns, in this order:

    [name='home']
    admin/
    users/
    users/

The current path, accounts/login/, didn't match any of these.

You're seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

----------------
