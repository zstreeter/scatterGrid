#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("Pypi_README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read()

setup_requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Zachary Streeter",
    author_email="zlstreeter@lbl.gov",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Exterior Complex Scaling Finite-Element Method Discrete Variable Representation grid for general physics problems.",
    entry_points={
        "console_scripts": [
            "quantumgrid=quantumgrid.cli:main",
            "ecs_femdvr_time_dep_h2=quantumgrid_examples.ECS_FEMDVR_diatomic_time_dep_vibration_H2:main",
            "ecs_femdvr_time_indep_h2=quantumgrid_examples.ECS_FEMDVR_diatomic_time_indep_vibration_H2:main",
            "femdvr_vib_states_h2=quantumgrid_examples.H2_vib_states_FEM_DVR:main",
            "femdvr_vib_states_co=quantumgrid_examples.CO_vib_states_FEM_DVR:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="quantumgrid",
    name="quantumgrid",
    packages=find_packages(
        include=["quantumgrid", "femdvr.py", "potential.py", "quantumgrid_examples",]
    ),
    package_data={"quantumgrid_examples": ["*.dat"],},
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/zstreeter/quantumgrid",
    version="2.0.010",
    zip_safe=False,
)
