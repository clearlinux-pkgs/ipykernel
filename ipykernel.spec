#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipykernel
Version  : 5.5.3
Release  : 58
URL      : https://files.pythonhosted.org/packages/03/ea/bd6b7df2557fbc40640b30102bc792b754964dafcd30d3acbd82b64c4cf5/ipykernel-5.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/03/ea/bd6b7df2557fbc40640b30102bc792b754964dafcd30d3acbd82b64c4cf5/ipykernel-5.5.3.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipykernel-license = %{version}-%{release}
Requires: ipykernel-python = %{version}-%{release}
Requires: ipykernel-python3 = %{version}-%{release}
Requires: ipython
Requires: jupyter_client
Requires: tornado
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pexpect
BuildRequires : python-dateutil
BuildRequires : tornado
BuildRequires : traitlets

%description
# IPython Kernel for Jupyter
This package provides the IPython kernel for Jupyter.

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
Provides: pypi(ipykernel)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the ipykernel package.


%prep
%setup -q -n ipykernel-5.5.3
cd %{_builddir}/ipykernel-5.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617213762
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipykernel
cp %{_builddir}/ipykernel-5.5.3/COPYING.md %{buildroot}/usr/share/package-licenses/ipykernel/a8d9e56558dabe10c8e716d79a4b01dcb6cf950f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/share/jupyter/kernels/python3/logo-64x64.png
rm -f %{buildroot}/usr/share/jupyter/kernels/python3/logo-32x32.png
rm -f %{buildroot}/usr/share/jupyter/kernels/python3/kernel.json

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipykernel/a8d9e56558dabe10c8e716d79a4b01dcb6cf950f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
