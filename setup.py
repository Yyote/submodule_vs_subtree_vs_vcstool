from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

# Explicitly list all subpackages to ensure correct installation layout
package_list = [
    'dependency',
]

setup_args = generate_distutils_setup(
    packages=package_list,
    package_dir={'': 'scripts'},
)

setup(**setup_args)
