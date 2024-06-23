from setuptools import find_packages, setup


setup(
    name='qr-code',
    version='0.0.1',
    description='Python script that convert public URLs into QR images.',
    author='Nesrine',
    author_email='Nesrine@email.com',
    install_requires=[],
    packages=find_packages(exclude=['doc*', 'tests*']),
    include_package_data=True,  
    zip_safe=False
)
