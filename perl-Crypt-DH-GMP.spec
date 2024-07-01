#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Crypt-DH-GMP
Version  : 0.00012
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-0.00012.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Crypt-DH-GMP-0.00012.tar.gz
Summary  : 'Crypt::DH Using GMP Directly'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Crypt-DH-GMP-perl = %{version}-%{release}
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
Provides: perl-Crypt-DH-GMP-devel = %{version}-%{release}
Requires: perl-Crypt-DH-GMP = %{version}-%{release}

%description dev
dev components for the perl-Crypt-DH-GMP package.


%package perl
Summary: perl components for the perl-Crypt-DH-GMP package.
Group: Default
Requires: perl-Crypt-DH-GMP = %{version}-%{release}

%description perl
perl components for the perl-Crypt-DH-GMP package.


%prep
%setup -q -n Crypt-DH-GMP-0.00012
cd %{_builddir}/Crypt-DH-GMP-0.00012

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Crypt::DH::GMP.3
/usr/share/man/man3/Crypt::DH::GMP::Compat.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
