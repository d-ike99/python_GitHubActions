import os
from setuptools import setup


PKGNAME = 'dike_test'

packages = []
for root, dirs, _ in os.walk(PKGNAME, followlinks=True):
    if 'tests' in root:
        continue
    packages += [os.path.join(root, dir_name) for dir_name in dirs if 'tests' not in dir_name]


setup(
    name=PKGNAME,
    version='1.0',
    author='dike',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.5',

)
