from setuptools import setup

setup(
    name='goto',
    version='0.1',
    py_modules=['goto'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        goto=scripts.goto:cli
    ''',
)
