#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : talloc
Version  : 2.4.0
Release  : 68
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
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697227814
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --disable-rpath \
--disable-rpath-install
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697227814
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/talloc.h
/usr/lib64/libpytalloc-util.cpython-312-x86-64-linux-gnu.so
/usr/lib64/libtalloc.so
/usr/lib64/pkgconfig/pytalloc-util.cpython-312-x86_64-linux-gnu.pc
/usr/lib64/pkgconfig/talloc.pc

%files extras
%defattr(-,root,root,-)
/usr/include/pytalloc.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpytalloc-util.cpython-312-x86-64-linux-gnu.so.2
/usr/lib64/libpytalloc-util.cpython-312-x86-64-linux-gnu.so.2.4.0
/usr/lib64/libtalloc.so.2
/usr/lib64/libtalloc.so.2.4.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
