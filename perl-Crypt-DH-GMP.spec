#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-DH-GMP
Version  : 0.00012
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-0.00012.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-0.00012.tar.gz
Summary  : 'Crypt::DH Using GMP Directly'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Crypt-DH-GMP-lib = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : gmp-dev
BuildRequires : perl(Module::Install)
BuildRequires : perl(Test::Requires)
BuildRequires : perl-Devel-CheckLib

%description
No detailed description available

%package dev
Summary: dev components for the perl-Crypt-DH-GMP package.
Group: Development
Requires: perl-Crypt-DH-GMP-lib = %{version}-%{release}
Provides: perl-Crypt-DH-GMP-devel = %{version}-%{release}

%description dev
dev components for the perl-Crypt-DH-GMP package.


%package lib
Summary: lib components for the perl-Crypt-DH-GMP package.
Group: Libraries

%description lib
lib components for the perl-Crypt-DH-GMP package.


%prep
%setup -q -n Crypt-DH-GMP-0.00012

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Crypt/DH/GMP.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Crypt/DH/GMP/Compat.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::DH::GMP.3
/usr/share/man/man3/Crypt::DH::GMP::Compat.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/Crypt/DH/GMP/GMP.so
