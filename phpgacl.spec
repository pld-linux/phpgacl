# TODO
# - unpack and install other_languages/perl/perlGACL-check-1.0.tar.gz
Summary:	A PHP class offering a simple and powerful "drop in" permission system
Summary(pl.UTF-8):   Klasa PHP oferująca prosty i potężny system uprawnień
Name:		phpgacl
Version:	3.3.4
Release:	0.2
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/phpgacl/%{name}-%{version}.tar.gz
# Source0-md5:	6a5e1e02ea38fa55b57969bd161ec2e0
Patch0:		%{name}-adodb.patch
Patch1:		%{name}-cache_lite.patch
URL:		http://phpgacl.sourceforge.net/
Requires:	adodb >= 4.67-1.17
Requires:	php-common >= 3:4.0.0
Requires:	php-pear-Cache_Lite >= 1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpGACL is an set of functions that allows you to apply access control
to arbitrary objects (web pages, databases, etc) by other arbitrary
objects (users, remote hosts, etc). It offers fine-grained access
control with simple management, and is very fast. It is written in PHP
(hence phpGACL), a popular scripting language that is commonly used to
dynamically create web pages. The GACL part of phpGACL stands for
Generic Access Control List.

%description -l pl.UTF-8
phpGACL to zestaw funkcji oferujących kontrolę dostępu do dowolnych
obiektów (stron WWW, baz danych itp.) przez inne dowolne obiekty
(użytkowników, zdalne hosty itp.). Zapewnia on dobrze dopasowaną
kontrolę dostępu z prostym zarządzaniem i jest szybki. Został napisany
w PHP (stąd nazwa phpGACL) - popularnym języku skryptowym powszechnie
używanym do dynamicznego tworzenia stron WWW. GACL z nazwy phpGACL
oznacza "Generic Access Control List" (ogólną listę kontroli dostępu).

%package perl
Summary:	Perl access for phpGACL
Summary(pl.UTF-8):   Dostęp z Perla do phpGACL
Group:		Development/Libraries

%description perl
This is example of Perl access for phpGACL.

%description perl -l pl.UTF-8
To jest przykład dostępu z Perla do phpGACL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
rm -rf adodb
rm -f Cache_Lite/{LICENSE,Lite.php}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/{%{name},%{name}-perl}

cp -r Cache_Lite admin soap test_suite $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r other_languages $RPM_BUILD_ROOT%{_datadir}/%{name}-perl

install *.php *.inc *.xml $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGELOG FAQ README TODO
%doc docs/
%{_datadir}/%{name}

%files perl
%defattr(644,root,root,755)
%{_datadir}/phpgacl-perl/other_languages
