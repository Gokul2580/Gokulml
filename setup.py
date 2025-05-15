from setuptools import setup, find_packages

setup(
    name='gokulml',
    version='0.1.0',
    description='Run and copy programs easily with a single import',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Goks',
    author_email='dm@gokulba.in',
    url='https://github.com/Gokul2580/Gokulml',
    packages=find_packages(),
    include_package_data=True,
    package_data={'gokulml': ['programs/*.py']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)