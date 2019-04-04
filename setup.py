from setuptools import setup
import sys
import json


PY2 = sys.version_info.major == 2
with open('metadata.json', **({} if PY2 else {'encoding': 'utf-8'})) as fp:
    metadata = json.load(fp)


setup(
    name='lexibank_bantubvd',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['lexibank_bantubvd'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'lexibank.dataset': [
            'bantubvd=lexibank_bantubvd:Dataset',
        ]
    },
    install_requires=[
<<<<<<< HEAD
        'pylexibank>=1.0',
=======
        'pylexibank>=0.11',
>>>>>>> dba82f65348cf9c68a89e2ffd0b0f6f01281f275
    ]
)
