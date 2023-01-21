from setuptools import setup, find_packages

setup(
    name='drf_mfcam',
    version='0.1a',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A mixin that adds the choices action to the ModelViewSet',
    url='https://github.com/milano-slesarik/drf_mfcam',
    author='Milano Slesarik',
    author_email='milslesarik@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'Django>=3.1',
        'djangorestframework>=3.11'
    ],
)
