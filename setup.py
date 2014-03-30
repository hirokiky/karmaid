from setuptools import setup, find_packages

setup(
    name='karmaid',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    url='http://karmaid.org/',
    license='AGPLv3',
    author='hirokiky',
    author_email='hirokiky@gmail.com',
    description='Karma ++/-- for everything',
    zip_safe=False,
    install_requires=[
        'pyramid==1.4.5',
        'pyramid_debugtoolbar',
        'waitress',
        'redis==2.9.1',
    ],
    entry_points="""\
    [paste.app_factory]
    main = karmaid:main
    """,
)
