===========
django-nuit
===========

A front-end framework based upon `Zurb Foundation`_ for Django applications, designed for a consistent look and feel across multiple apps and projects.

Documentation can be found at `Read the Docs`_.

===========
Quick Start
===========

Get started with Nuit by following these steps:

* Install Nuit with ``pip``::

    pip install django-nuit

* Add ``nuit`` to your ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'nuit',
        ...
    )

* Nuit relies on django-autoconfig_, which requires the following at the end of ``settings.py``::

    from django_autoconfig.autoconfig import configure_settings
    configure_settings(globals())

* In a production environment, add the following setting for django-pipeline_ (see their documentation for more details)::

    PIPELINE_ENABLED = True

* Install the SASS binary in order to compile and compress the CSS. This can't be installed using ``pip``, and will need to be installed manually (usually with ``gem install sass``)

* Run ``collectstatic``::

    manage.py collectstatic

You're now ready to start using Nuit in your templates and apps. Read the `documentation <https://django-nuit.readthedocs.org/en/latest/>`_ for the next steps.

============
Contributing
============

To contribute, fork the repo, do your work, and issue a pull request. We ask that contributors adhere to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ standards, and include full tests for all their code.

.. _`Zurb Foundation`: http://foundation.zurb.com
.. _`Read the Docs`: http://django-nuit.readthedocs.org/en/latest
.. _`django-autoconfig`: http://github.com/mikebryant/django-autoconfig/
.. _`django-pipeline`: https://django-pipeline.readthedocs.org/en/latest/
