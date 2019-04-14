# Created by pyp2rpm-1.0.1
%global pypi_name mccabe

Name:           python-mccabe
Version:        0.6.1
Release:        10
Group:          Development/Python
Summary:        McCabe checker, plugin for flake8
License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://pypi.io/packages/source/m/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  python2dist(setuptools)
BuildRequires:  python2-devel

%description
McCabe complexity checker
=========================

Ned's script to check
McCabe complexity.

This module provides a plugin for ``flake8``, the Python
code checker.

%package -n python2-%{pypi_name}
Group:          Development/Python
Summary:        McCabe checker, plugin for flake8
BuildArch:      noarch
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
McCabe complexity checker
=========================

Ned's script to check
McCabe complexity.

This module provides a plugin for ``flake8``, the Python
code checker.

%prep
%setup -q -n %{pypi_name}-%{version}

cp -a . %{py3dir}

%build
%py2_build
pushd %{py3dir}
%py3_build
popd

%install
%py2_install
pushd %{py3dir}
%py3_install
popd

%files -n python2-%{pypi_name}
%doc LICENSE
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitelib}/%{pypi_name}.py*

%files
%doc LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/*
