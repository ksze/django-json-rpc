# -*- coding: utf-8 -*-

# Django
try:
    # Django pre-1.6
    from django.conf.urls.defaults import patterns, url
except ImportError:
    # Django 1.6 and later
    from django.conf.urls import patterns, url

# jsonrpc
from jsonrpc.site import jsonrpc_site

# the JSON-RPC methods
from .methods import (
        echo, echoAuth, notify, fails, strangeEcho, safeEcho, strangeSafeEcho,
        protectedEcho, protectedArgsEcho, protectedReturnEcho, authCheckedEcho,
        checkedVarArgsEcho,
    )

# Register the JSON-RPC methods:

for method in (
        echo, echoAuth, notify, fails, strangeEcho, safeEcho, strangeSafeEcho,
        protectedEcho, protectedArgsEcho, protectedReturnEcho, authCheckedEcho,
        checkedVarArgsEcho,
    ):
    jsonrpc_site.register(method)

urlpatterns = patterns('',
  url(r'^json/browse/$', 'jsonrpc.views.browse', name='jsonrpc_browser'),
  url(r'^json/$', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
  (r'^json/(?P<method>[a-zA-Z0-9.-_]+)$', jsonrpc_site.dispatch),
)
