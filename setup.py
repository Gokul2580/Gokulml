from setuptools import setup, find_packages

setup(
    name='gokulml',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'gokulml': ['programs/*.py'],
    },
    description='GokulML Python Program Runner',
    author='Goks',
    author_email='your@email.com',
    keywords=['gokul', 'program runner', 'gokulml'],
)
