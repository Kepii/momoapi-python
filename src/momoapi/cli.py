"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mmomoapi_python` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``momoapi_python.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``momoapi_python.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
import requests
import uuid


def generateToken(host, key):
    data = {"providerCallbackHost": host}
    token = uuid.uuid4()
    headers = {
        "X-Reference-Id": "%s" % token,
        "Content-Type": "application/json",
        "Ocp-Apim-Subscription-Key": "%s" % key
    }
    r = requests.post("https://ericssonbasicapi2.azure-api.net/v1_0/apiuser", data=data, headers=headers)

    return "Your token is %s : your secret key is : %s" % (token, r.text)


@click.command()
@click.option('--provider', prompt="providerCallBackHost", help='providerCallBackHost')
@click.option('--key', prompt="Ocp-Apim-Subscription-Key", help='Ocp-Apim-Subscription-Key')
def main(provider, key):
    click.echo(generateToken(provider, key))