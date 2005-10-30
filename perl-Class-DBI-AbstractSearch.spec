#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-AbstractSearch
Summary:	Class::DBI::AbstractSearch - Abstract Class::DBI's SQL with SQL::Abstract::Limit
Name:		perl-Class-DBI-AbstractSearch
Version:	0.07
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d40e7301201135fe0246251097132a54
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::DBI) >= 0.9
BuildRequires:	perl(SQL::Abstract::Limit) >= 0.1
BuildRequires:	perl(Test::More) >= 0.32
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::AbstractSearch is a Class::DBI plugin to glue
SQL::Abstract::Limit into Class::DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/AbstractSearch.pm
%{_mandir}/man3/*
