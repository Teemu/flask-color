from setuptools import setup


setup(
    name='Flask-Color',
    version='0.2.1',
    url='https://github.com/Frozenball/flask-color',
    license='MIT',
    author='Frozenball',
    author_email='orkkiolento@gmail.com',
    description='flask-color is an extension for Flask that improves the built-in web server with colors when debugging. Unnecessary clutter such as time or IP are hidden.',
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
