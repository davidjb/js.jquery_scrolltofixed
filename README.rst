js.jquery_scrolltofixed
***********************

Introduction
============

This library packages `ScrollToFixed (jQuery plugin)`_ for `fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`ScrollToFixed (jQuery plugin)`: http://bigspotteddog.github.com/ScrollToFixed/

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.jquery_scrolltofixed``) are published to some URL.

Packaging
=========

The packaging is stored on GitHub at
https://github.com/davidjb/js.jquery_scrolltofixed. If you happen to come
across a bug that corresponds to *packaging*, then please report it here. Pull
requests are more than welcome if you're fixing something yourself -- the more
help the better!

Any other bugs that relate to the library itself should be directed to the
original developers.

Updating this package
=====================

This library currently does not have any form of specific versioning. So,
version numbers can be roughly arbitrary.

In order to obtain a newer version of this library, do the following::

    git clone git://github.com/davidjb/js.jquery_scrolltofixed.git
    cd js.jquery_scrolltofixed
    pushd js/jquery_scrolltofixed/resources/
    wget https://github.com/bigspotteddog/ScrollToFixed/raw/master/jquery-scrolltofixed-min.js -O jquery-scrolltofixed-min.js 
    wget https://github.com/bigspotteddog/ScrollToFixed/blob/master/jquery-scrolltofixed.js -O jquery-scrolltofixed.js
    #Edit version and change log
    git commit -a -m "Updated to git version #hash"
    git push

If you're doing this out in your own fork of the GitHub repository, then send
through a pull request so everyone can benefit.

