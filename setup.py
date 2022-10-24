import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012022S2JNSA1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# docassemble.LLAW33012022S2JNSA1\r\n\r\nA docassemble extension.\r\n\r\n# Application description\r\nJusticeGuide SA is a service directory for JusticeNet (a not-for-profit enterprise). It aims to connect clients with legal issues to the relevant organisations applicable to the circumstances of their personal issue, and related financial and social circumstances. JusticeGuide SA acts as a bridge between those in need and those who can help. It is necessary to address the gap between the average person of limited technological knowledge, and the legal profession. The application categorises information from clients to help them identify appropriate services.\r\n\r\nThe application exists as a filter that ensures those reaching out to JusticeNet SA do so as a last resort due to ineligibility for other legal services. JusticeNet SA typically works with those of varied ages from 19 years or older and JusticeGuide SA ensures users of non-technological backgrounds are able to feel connected and heard.\r\n\r\nJusticeGuide SA is a program that primarily functions as an interactive service directory that displays relevant organisations to the users’ issues based on data input.\r\n\r\n\r\n\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Lauren Docking',
      author_email='dock0013@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012022S2JNSA1/', package='docassemble.LLAW33012022S2JNSA1'),
     )

