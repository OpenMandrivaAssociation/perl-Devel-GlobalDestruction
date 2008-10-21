%define module   Devel-GlobalDestruction
%define version    0.02
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Expose PL_dirty, the flag which marks global
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Devel/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Scope::Guard)
BuildRequires: perl(Sub::Exporter)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happenning you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_mandir}/man3/*
%perl_vendorlib/*


