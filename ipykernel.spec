#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipykernel
Version  : 4.6.1
Release  : 4
URL      : https://pypi.python.org/packages/0c/41/67e16b243b78b49f4b1650d045b63be187c27d20a76f0f7b8e61e0fcb966/ipykernel-4.6.1.tar.gz
Source0  : https://pypi.python.org/packages/0c/41/67e16b243b78b49f4b1650d045b63be187c27d20a76f0f7b8e61e0fcb966/ipykernel-4.6.1.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipykernel-python
Requires: ipykernel-data
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

%description python
python components for the ipykernel package.


%prep
%setup -q -n ipykernel-4.6.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492009648
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
/usr/share/jupyter/kernels/python3/kernel.json
/usr/share/jupyter/kernels/python3/logo-32x32.png
/usr/share/jupyter/kernels/python3/logo-64x64.png

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
