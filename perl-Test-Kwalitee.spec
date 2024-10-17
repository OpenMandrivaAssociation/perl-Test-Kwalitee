%define upstream_name    Test-Kwalitee
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Test the Kwalitee of a distribution before you release it
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-version
BuildRequires:	perl(Module::CPANTS::Analyse)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description 
Kwalitee is an automatically-measurable gauge of how good your software is.
That's very different from quality, which a computer really can't measure in a
general sense. (If you can, you've solved a hard problem in computer science.)

In the world of the CPAN, the CPANTS project (CPAN Testing Service; also a
funny acronym on its own) measures Kwalitee with several metrics. If you plan
to release a distribution to the CPAN -- or even within your own organization
-- testing its Kwalitee before creating a release can help you improve your
quality as well.

Test::Kwalitee and a short test file will do this for you automatically.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc ChangeLog README
%{perl_vendorlib}/Test
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 405552
- rebuild using %%perl_convert_version

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 272270
- update to new version 1.01

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.30-2mdv2008.1
+ Revision: 133821
- kill re-definition of %%buildroot on Pixel's request


* Thu Nov 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2007.0
+ Revision: 88921
- Import perl-Test-Kwalitee

* Sat Nov 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2007.1
- first mdv release

