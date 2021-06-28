from setuptools import setup, find_packages

setup(
    name='ai',
    version='1.0',
    description='FSD Car Simulation',
    url='https://github.com/J-Obog/ai-car',
    author='JObog',
    author_email='jobogbaimhe@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['examples', 'tests'])
)