# YouTube API v3 for a Django project

A simple API that requests access to manage a user's youtube account from within a `Django` project.

(I successfully made API calls inside `jupyter notebook` running inside a virtual environment in windows 10. Here's how to use `jupyter notebook` within a virtual environment in windows 10 (You should try for your own version of windows).

## Running jupyter notebook within a python virtual environment in windows (not required)

Create the virtual environment and activate it. (Skip this section if you are familiar with working with virtual environments. Otherwise, see this [gist](https://gist.github.com/immensity/d66fec9eed65fd1aa7b85530c70ad0e5) for some directions.

Now install the required libraries

    $ pip install tornado
    $ pip install jupyter
    $ python -m ipykernel install --user --name myenv --display-name "name_for_the_newly_installed_jupyter_kernel"

The `--display-name` flag is optional.

Now when you open a jupyter notebook and click `Kernel` `>` `Change kernel` dropdown,  your virtual environment appears in  the list of kernels.

Also, to launch jupyter notebook in a directory, just `cd` into the directory on your command line and run 

    $ jupyter notebook

## Setting up the project and necessary keys

The YouTube API v3 (and perhaps most google APIs), for all its simplicity, can be pretty confusing if you're coming to it for the first time. The key thing is understanding `input` and `output` data structures. Here are the steps.

1. The absolute first thing you need to do is to visit [developer console](https://console.developers.google.com/) and create a project. You may be asked to accept some terms. Accept the terms and continue.

1. After creating the project, the next thing you need to do is to actually create the credentials you need to access the API. On the LHS (Left Hand Side) of the screen click on `Credentials`. Then click on `Create credentials` dropdown. Now you have to choose what type of credentials you want to create. For an explanation of credentials type, see this excellent [post](https://www.daimto.com/google-developer-console-create-public-api-key/).

1. Creating an `API Key` is very straightforward. To create an `OAuth client ID` you first need to configure the consent screen. This is the message that will be shown to the user when your app requests their consent to access their data. In the `credentials` screen, just beside `credentials` on the page is `OAuth consent screen`. Click on it and configure it as you wish. The only required options are the `Product name shown to users` and `Authorized redirect URIs`. All others are optional. After this step you'll now be able to create an `OAuth client ID` for the `Web application` type.

1. For this project use both `API Key` and `OAuth client ID`. For `OAuth client ID` I'll be using a `Web application` as my application type because my API calls will be originating from a `Django` web server.

1. Now go back into your virtual environment (or wherever you wish to use the API) and install these libraries

    `pip install --upgrade google-auth`

    `pip install --upgrade google-api-python-client`

    `pip install google_auth_oauthlib`

    `pip install google-auth-httplib2`

## Additional setup
**Replace these when you clone the repo**

1. API_KEY, CHANNEL_ID found in `youtube/api_calls.py`
1. CLIENT_SECRETS_FILE location. This is made use of in `youtube/views.py`. Make sure to download your `client_secret.json` file and place it in the `youtube/credentials/` directory. You can always move this file somewhere else, but then you need to modify this line `CLIENT_SECRETS_FILE = "youtube/credentials/client_secret.json"` in the `youtube/views.py` file. The `client_secret.json` file is available for download in your project.

## Resources

1. Youtube API v3 [docs](https://developers.google.com/youtube/v3/docs)
1. [YouTube Data in Python](https://medium.com/greyatom/youtube-data-in-python-6147160c5833)
1. https://github.com/GoogleCloudPlatform/google-auth-library-python
1. https://github.com/google/google-api-python-client
1. https://github.com/GoogleCloudPlatform/google-auth-library-python-oauthlib
1. https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
1. https://developers.google.com/youtube/v3/guides/auth/server-side-web-apps
