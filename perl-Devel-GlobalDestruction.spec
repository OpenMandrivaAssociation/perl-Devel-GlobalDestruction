%define modname	Devel-GlobalDestruction
%define modver 0.14

Summary:	Expose PL_dirty, the flag which marks global
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Devel::GlobalDestruction
Source0:	http://www.cpan.org/modules/by-module/Devel/Devel-GlobalDestruction-%{modver}.tar.gz
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
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

#%check
#make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*


