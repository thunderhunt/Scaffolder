import setuptools

setuptools.setup(
    name="scaffolder",
    version="1.0.0",
    author="Rahan Sharma",
    packages=[],
    entry_points={
        'console_scripts':[
            'scaffolder=scaffolder:main'
        ]
    },
    description="Tool used to create scaffolding, based on the supplied configuration YAML.",
    long_description_content_type="text/markdown",
    url="https://github.com/Thunderhunt/scaffolder",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "PyYAML"
    ],
)
