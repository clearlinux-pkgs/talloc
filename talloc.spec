#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : talloc
Version  : 2.4.0
Release  : 67
URL      : https://www.samba.org/ftp/talloc/talloc-2.4.0.tar.gz
Source0  : https://www.samba.org/ftp/talloc/talloc-2.4.0.tar.gz
Summary  : A hierarchical pool based memory system with destructors
Group    : Development/Tools
License  : LGPL-3.0+
Requires: talloc-lib = %{version}-%{release}
Requires: talloc-python = %{version}-%{release}
Requires: talloc-python3 = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : buildreq-configure
BuildRequires : libaio-dev
BuildRequires : python3-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-add-mock-disable-static-option.patch

%description
See http://code.google.com/p/waf/ for more information on waf
You can get a svn copy of the upstream source with:

%package dev
Summary: dev components for the talloc package.
Group: Development
Requires: talloc-lib = %{version}-%{release}
Provides: talloc-devel = %{version}-%{release}
Requires: talloc = %{version}-%{release}

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
%setup -q -n talloc-2.4.0
cd %{_builddir}/talloc-2.4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1683252960
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --disable-rpath \
--disable-rpath-install
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1683252960
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/talloc.h
/usr/lib64/libtalloc.so
/usr/lib64/pkgconfig/talloc.pc

%files extras
%defattr(-,root,root,-)
/usr/include/pytalloc.h
/usr/lib64/libpytalloc-util.cpython-311-x86-64-linux-gnu.so*
/usr/lib64/pkgconfig/pytalloc-util.cpython-311-x86_64-linux-gnu.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtalloc.so.2
/usr/lib64/libtalloc.so.2.4.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
