#
#
Summary:	A PHP class offering a simple and powerful "drop in" permission system
Summary(pl):	Klasa PHP oferuj±ca prosty i potê¿ny system uprawnieñ
Name:		phpgacl
Version:	3.3.4
Release:	0.1
Epoch:		0
License:	LGPL
#Vendor:		-
Group:		Development/Libraries
#Icon:		-
Source0:	http://dl.sourceforge.net/phpgacl/%{name}-%{version}.tar.gz
# Source0-md5:	6a5e1e02ea38fa55b57969bd161ec2e0
#Patch0:		%{name}-what.patch
URL:		http://phpgacl.sourceforge.net/
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
Requires:	php >= 4
Requires:	adodb
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
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

%description -l pl
phpGACL to zestaw funkcji oferuj±cych kontrolê dostêpu do dowolnych
obiektów (u¿yszkodników, zdalnych hostów, itp). Zapewnia on dobrze
dopasowan± kontrolê dostêpu z prostym zarz±dzaniem i jest szybki.
Zosta³ napisany w PHP (st±d nazwa phpGACL), popularnym jêzyku
skryptowym.

%package perl
Summary:	perl access for phpGACL
Summary(pl):	dostêp z perla do phpGACL
Version:	3.3.4
Release:	0.1
Group:		Development/Libraries

%description perl
This is example of perl access for phpGACL

%description perl -l pl
To jest przyk³ad dostêpu z perla do phpGACL

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT/%{_datadir}/{%{name},%{name}-perl}

cp -r Cache_Lite admin soap test_suite $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -r other_languages $RPM_BUILD_ROOT/%{_datadir}/%{name}-perl

install *.php *.inc *.xml $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS CHANGELOG FAQ README TODO
%doc docs/

%{_datadir}/%{name}

# initscript and its config

%files perl
%defattr(644,root,root,755)
#%doc extras/*.gz
%{_datadir}/phpgacl-perl/other_languages
