Name:           python-mccabe
Version:	0.7.0
Release:	5
Group:          Development/Python
Summary:        McCabe checker, plugin for flake8
License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/m/mccabe/mccabe-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
Obsoletes:	python2-mccabe < %{EVRD}

%description
McCabe complexity checker
=========================

Ned's script to check
McCabe complexity.

This module provides a plugin for ``flake8``, the Python
code checker.

%prep -a
sed -i -e "/setup_requires=\['pytest-runner'\],/d" setup.py

%files
%doc LICENSE
%{python_sitelib}/mccabe-%{version}-py*.*.egg-info 
%{python_sitelib}/mccabe.py
