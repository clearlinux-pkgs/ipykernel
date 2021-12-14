#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipykernel
Version  : 6.6.0
Release  : 83
URL      : https://files.pythonhosted.org/packages/60/30/cf3867ce0dee0a7230ec5eb85232136c3875688816ad355a7b65f4f4e8ef/ipykernel-6.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/30/cf3867ce0dee0a7230ec5eb85232136c3875688816ad355a7b65f4f4e8ef/ipykernel-6.6.0.tar.gz
Summary  : IPython Kernel for Jupyter
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: ipykernel-license = %{version}-%{release}
Requires: ipykernel-python = %{version}-%{release}
Requires: ipykernel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : importlib_metadata
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pexpect
BuildRequires : pypi(debugpy)
BuildRequires : pypi(ipython)
BuildRequires : pypi(jupyter_client)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(matplotlib_inline)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(tornado)
BuildRequires : pypi(traitlets)
BuildRequires : pypi(wheel)
BuildRequires : python-dateutil

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
Requires: pypi(debugpy)
Requires: pypi(ipython)
Requires: pypi(jupyter_client)
Requires: pypi(matplotlib_inline)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the ipykernel package.


%prep
%setup -q -n ipykernel-6.6.0
cd %{_builddir}/ipykernel-6.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638452399
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipykernel
cp %{_builddir}/ipykernel-6.6.0/COPYING.md %{buildroot}/usr/share/package-licenses/ipykernel/a8d9e56558dabe10c8e716d79a4b01dcb6cf950f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-64x64.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/logo-32x32.png
rm -f %{buildroot}*/usr/share/jupyter/kernels/python3/kernel.json

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
