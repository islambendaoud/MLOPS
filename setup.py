from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='sentiment_analyzer',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={"":"src"},    
    install_requires=required,
    entry_points={
        'console_scripts': [
            'predict = sentiment_analyzer.predict:predict' , 
            'promote  = sentiment_analyzer.promote:promote' ,
            'retrain = sentiment_analyzer.retrain:retrain' , 
            'hf_export = sentiment_analyzer.hf_export:hf_export', 
        ],
    },
)