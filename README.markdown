# BLOGLY :ribbon: :scroll:

***A small Django-powered app to make a blog. :ribbon: :scroll:***

## ABOUT :books:

Since I wanted to show off my Django skills and it toook me ages to come up with an idea, I thought it'd be a good idea to make a small app that shows how to build a blog using Django and SQLite. Enjoy. :heart:

## USAGE

### Requirements

make sure you have the following tools installed and available from the command line:

- [Python](https://python.org)
- [Git](https://git-scm.org)

### Steps

To run this app on your own machine, execute these steps:

- 1.) Get the source code:

```bash
git clone https://github.com/angeldollface/blogly
````

- 2.) Install `virtualenv`:

```bash
python3 -m pip install virtualenv
```

- 3.) Change directory into *Blogly*'s root:

```bash
cd blogly
````

- 4.) Create a new virtual environment here:

```bash
python3 -m venv .
```

- 5.) Activate the virtual environment (The command below is for `*nix` systems. Do the equivalent for this on Windows.):

```bash
source bin/activate
```

- 6.) Install the project's dependencies:

```bash
python -m pip install -r requirements.txt
```

- 7.) Setup the database migrations:

```bash
python manage.py --run-syncdb
```

- 8.) Setup a superuser account:

```bash
python manage.py createsuperuser
```

- 9.) Run the local development server:

```bash
python manage.py runserver
```

- 10.) Visit the address on which the local server is running and add `/admin` to the end of that URL.

- 11.) Login.

- 12.) Click the `+` next to the `Posts` text.

- 13.) Write a blog post.

- 14.) Logout.

- 15.) Go back to the root address.

- 16.) Behold your post!


## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.

## NOTE :scroll:

- *Blogly :ribbon: :scroll:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.
