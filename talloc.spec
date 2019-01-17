#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : talloc
Version  : 2.1.15
Release  : 26
URL      : https://www.samba.org/ftp/talloc/talloc-2.1.15.tar.gz
Source0  : https://www.samba.org/ftp/talloc/talloc-2.1.15.tar.gz
Summary  : A hierarchical pool based memory system with destructors
Group    : Development/Tools
License  : LGPL-3.0+
Requires: talloc-lib = %{version}-%{release}
Requires: talloc-python = %{version}-%{release}
Requires: talloc-python3 = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : libaio-dev
BuildRequires : python3-dev
BuildRequires : zlib-dev
Patch1: 0001-add-mock-disable-static-option.patch
Patch2: 0002_fix_finding_waf.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package dev
Summary: dev components for the talloc package.
Group: Development
Requires: talloc-lib = %{version}-%{release}
Provides: talloc-devel = %{version}-%{release}

%description dev
dev components for the talloc package.


%package extras
Summary: extras components for the talloc package.
Group: Default

%description extras
extras components for the talloc package.


%package lib
Summary: lib components for the talloc package.
Group: Libraries

%description lib
lib components for the talloc package.


%package python
Summary: python components for the talloc package.
Group: Default
Requires: talloc-python3 = %{version}-%{release}

%description python
python components for the talloc package.


%package python3
Summary: python3 components for the talloc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the talloc package.


%prep
%setup -q -n talloc-2.1.15
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547743348
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-rpath --disable-rpath-install
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1547743348
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libpytalloc-util.cpython-37m-x86-64-linux-gnu.so
/usr/lib64/libtalloc.so
/usr/lib64/pkgconfig/pytalloc-util.cpython-37m-x86_64-linux-gnu.pc
/usr/lib64/pkgconfig/talloc.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libpytalloc-util.cpython-37m-x86-64-linux-gnu.so.2
/usr/lib64/libpytalloc-util.cpython-37m-x86-64-linux-gnu.so.2.1.15

%files lib
%defattr(-,root,root,-)
%exclude /usr/lib64/libpytalloc-util.cpython-37m-x86-64-linux-gnu.so.2
%exclude /usr/lib64/libpytalloc-util.cpython-37m-x86-64-linux-gnu.so.2.1.15
/usr/lib64/libtalloc.so.2
/usr/lib64/libtalloc.so.2.1.15

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
