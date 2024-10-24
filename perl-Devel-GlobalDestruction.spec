%define modname	Devel-GlobalDestruction

Summary:	Expose PL_dirty, the flag which marks global
Name:		perl-%{modname}
Version:	0.14
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Devel::GlobalDestruction
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-GlobalDestruction-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl-devel

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happenning you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

#%check
#make test

%install
%make_install

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*


