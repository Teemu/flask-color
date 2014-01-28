from setuptools import setup


setup(
    name='Flask-Color',
    version='0.1',
    url='https://github.com/Frozenball/flask-color',
    license='MIT',
    author='Frozenball',
    author_email='orkkiolento@gmail.com',
    description='Colors the requests in debugging mode',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
