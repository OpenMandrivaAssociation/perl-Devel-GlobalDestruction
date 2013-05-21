%define upstream_name    Devel-GlobalDestruction
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Expose PL_dirty, the flag which marks global
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Scope::Guard)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happenning you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if
global destruction is in effect.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-3mdv2012.0
+ Revision: 765168
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.40.0-2
+ Revision: 763697
- rebuilt for perl-5.14.x

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.40.0-1
+ Revision: 688745
- update to new version 0.04

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.30.0-2
+ Revision: 667112
- mass rebuild

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 604715
- update to new version 0.03

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-3mdv2011.0
+ Revision: 555793
- rebuild for perl 5.12
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 403100
- rebuild using %%perl_convert_version

* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
+ Revision: 295956
- import perl-Devel-GlobalDestruction


* Tue Oct 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
- initial mdv release, generated with cpan2dist

