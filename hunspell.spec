#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hunspell
Version  : 1.7.0
Release  : 7
URL      : https://github.com/hunspell/hunspell/archive/v1.7.0.tar.gz
Source0  : https://github.com/hunspell/hunspell/archive/v1.7.0.tar.gz
Summary  : Spell checker and morphological analyzer library and program
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1 MPL-1.1
Requires: hunspell-bin = %{version}-%{release}
Requires: hunspell-lib = %{version}-%{release}
Requires: hunspell-license = %{version}-%{release}
Requires: hunspell-man = %{version}-%{release}

%description
# About Hunspell
Hunspell is a free spell checker and morphological analyzer library
and command-line tool, licensed under LGPL/GPL/MPL tri-license.

%package bin
Summary: bin components for the hunspell package.
Group: Binaries
Requires: hunspell-license = %{version}-%{release}
Requires: hunspell-man = %{version}-%{release}

%description bin
bin components for the hunspell package.


%package dev
Summary: dev components for the hunspell package.
Group: Development
Requires: hunspell-lib = %{version}-%{release}
Requires: hunspell-bin = %{version}-%{release}
Provides: hunspell-devel = %{version}-%{release}

%description dev
dev components for the hunspell package.


%package lib
Summary: lib components for the hunspell package.
Group: Libraries
Requires: hunspell-license = %{version}-%{release}

%description lib
lib components for the hunspell package.


%package license
Summary: license components for the hunspell package.
Group: Default

%description license
license components for the hunspell package.


%package man
Summary: man components for the hunspell package.
Group: Default

%description man
man components for the hunspell package.


%prep
%setup -q -n hunspell-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549255453
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1549255453
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hunspell
cp COPYING %{buildroot}/usr/share/package-licenses/hunspell/COPYING
cp COPYING.LESSER %{buildroot}/usr/share/package-licenses/hunspell/COPYING.LESSER
cp COPYING.MPL %{buildroot}/usr/share/package-licenses/hunspell/COPYING.MPL
cp license.hunspell %{buildroot}/usr/share/package-licenses/hunspell/license.hunspell
cp license.myspell %{buildroot}/usr/share/package-licenses/hunspell/license.myspell
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/affixcompress
/usr/bin/analyze
/usr/bin/chmorph
/usr/bin/hunspell
/usr/bin/hunzip
/usr/bin/hzip
/usr/bin/ispellaff2myspell
/usr/bin/makealias
/usr/bin/munch
/usr/bin/unmunch
/usr/bin/wordforms
/usr/bin/wordlist2hunspell

%files dev
%defattr(-,root,root,-)
/usr/include/hunspell/atypes.hxx
/usr/include/hunspell/hunspell.h
/usr/include/hunspell/hunspell.hxx
/usr/include/hunspell/hunvisapi.h
/usr/include/hunspell/w_char.hxx
/usr/lib64/libhunspell-1.7.so
/usr/lib64/pkgconfig/hunspell.pc
/usr/share/man/man3/hunspell.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhunspell-1.7.so.0
/usr/lib64/libhunspell-1.7.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hunspell/COPYING
/usr/share/package-licenses/hunspell/COPYING.LESSER
/usr/share/package-licenses/hunspell/COPYING.MPL
/usr/share/package-licenses/hunspell/license.hunspell
/usr/share/package-licenses/hunspell/license.myspell

%files man
%defattr(0644,root,root,0755)
/usr/share/man/hu/man1/hunspell.1
/usr/share/man/man1/hunspell.1
/usr/share/man/man1/hunzip.1
/usr/share/man/man1/hzip.1
/usr/share/man/man5/hunspell.5
