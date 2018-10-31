%define module mccabe
  
Summary:	McCabe checker, plugin for flake8
Name:		python-mccabe
Version:	0.6.1
Release:	2
Group:		Development/Python
License:	Python
Url:		https://pypi.python.org/pypi/mccabe
Source0:	https://pypi.python.org/packages/06/18/fa675aa501e11d6d6ca0ae73a101b2f3571a565e0f7d38e062eec18a91ee/mccabe-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildArch:	noarch
 
%description 
McCabe checker, plugin for flake8

%prep
%setup -qn %{module}-%{version}
  
%build
%__python setup.py build

%install 
%__python setup.py install --root=%{buildroot}

%files
%{py_puresitedir}/mccabe.py
%{py_puresitedir}/mccabe*.egg-info
%{py_puresitedir}/__pycache__/mccabe*
