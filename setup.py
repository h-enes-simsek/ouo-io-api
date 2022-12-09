from setuptools import setup, find_packages

setup(
    name='ouo-io-api',
    version='1.0',
    description='an api for the ouo.io link shortener service',
    long_description_content_type='text/x-rst',
    long_description=open('README.rst').read(),
    license='MIT',
    author="Hasan Enes Şimşek",
    author_email='enes1406@gmail.com',
    packages=['ouo'],
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable'
    ],
    url='https://github.com/h-enes-simsek/ouo-io-api',
    keywords='ouo,ouo-io,link-shortener',
    install_requires=[
        'requests'
    ],
    python_requires='>=3'
)