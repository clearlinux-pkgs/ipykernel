#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipykernel
Version  : 5.1.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/11/0b/95330660f8cc5d63428b9886c800ea8d68842fd866389cf579acca4915be/ipykernel-5.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/0b/95330660f8cc5d63428b9886c800ea8d68842fd866389cf579acca4915be/ipykernel-5.1.0.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipykernel-python3
Requires: ipykernel-license
Requires: ipykernel-data
Requires: ipykernel-python
Requires: ipython
Requires: jupyter_client
Requires: tornado
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pexpect
BuildRequires : python-dateutil
BuildRequires : tornado
BuildRequires : traitlets

%description
# IPython Kernel for Jupyter
This package provides the IPython kernel for Jupyter.

%package data
Summary: data components for the ipykernel package.
Group: Data

%description data
data components for the ipykernel package.


%package license
Summary: license components for the ipykernel package.
Group: Default

%description license
license components for the ipykernel package.


%package python
Summary: python components for the ipykernel package.
Group: Default
Requires: ipykernel-python3 = %{version}-%{release}

%description python
python components for the ipykernel package.


%package python3
Summary: python3 components for the ipykernel package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipykernel package.


%prep
%setup -q -n ipykernel-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539109117
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ipykernel
cp COPYING.md %{buildroot}/usr/share/doc/ipykernel/COPYING.md
python3 -tt setup.py build  install --root=%{buildroot}
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

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/ipykernel/COPYING.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
