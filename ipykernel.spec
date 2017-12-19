#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipykernel
Version  : 4.7.0
Release  : 10
URL      : http://pypi.debian.net/ipykernel/ipykernel-4.7.0.tar.gz
Source0  : http://pypi.debian.net/ipykernel/ipykernel-4.7.0.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipykernel-python3
Requires: ipykernel-data
Requires: ipykernel-python
BuildRequires : ipython
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pip
BuildRequires : python-dateutil
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# IPython Kernel for Jupyter
This package provides the IPython kernel for Jupyter.

%package data
Summary: data components for the ipykernel package.
Group: Data

%description data
data components for the ipykernel package.


%package python
Summary: python components for the ipykernel package.
Group: Default
Requires: ipykernel-python3

%description python
python components for the ipykernel package.


%package python3
Summary: python3 components for the ipykernel package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipykernel package.


%prep
%setup -q -n ipykernel-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1512654484
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
%exclude /usr/share/jupyter/kernels/python3/kernel.json
%exclude /usr/share/jupyter/kernels/python3/logo-32x32.png
%exclude /usr/share/jupyter/kernels/python3/logo-64x64.png

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
