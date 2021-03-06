# TODO
# - use system creole, propel, phing packages (or better do not do that to avoid incompatibilities?)
# - php deps autofinder finds a lot of crap (that's why we use manual R now), maybe there is a way to improve
%define		pkgname	symfony-lexpress
%define		php_min_version	5.3.4
#include	/usr/lib/rpm/macros.php
Summary:	Open-source PHP web framework
Summary(pl.UTF-8):	Szkielet aplikacji WWW w PHP o otwartych źródłach
Name:		php-%{pkgname}
Version:	1.5.10
Release:	1
License:	various free licenses (distributable)
Group:		Development/Languages/PHP
Source0:	https://github.com/LExpress/symfony1/archive/v%{version}.tar.gz
# Source0-md5:	a864bb61f8b9ac78514297d3d36f9016
URL:		https://github.com/LExpress/symfony1/
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	Smarty
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php-pear-Archive_Tar
Requires:	php-pear-Log
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear Doctrine/.* PHPUnit/.* PHPUnit2/.* phing/.* propel/.* simpletest/.*

%description
This is fork of Symfony 1.4.

Based on the best practices of web development, thoroughly tried on
several active websites, symfony aims to speed up the creation and
maintenance of web applications, and to replace the repetitive coding
tasks by power, control and pleasure.

Symfony provides a lot of features seamlessly integrated together,
such as:
- simple templating and helpers
- cache management
- smart URLs
- scaffolding
- multilingualism and I18N support
- object model and MVC separation
- Ajax support
- enterprise ready

This is LExpress fork of no longer maintained official symfony 1.

%description -l pl.UTF-8
Oparty na najlepszych praktykach tworzenia aplikacji WWW, gruntownie
wypróbowany na kilku aktywnych serwisach moduł symfony próbuje
przyspieszyć tworzenie i utrzymywanie aplikacji WWW oraz zastąpić
powtarzające się zadania kodowania potęgą, kontrolą i przyjemnością.

Symfony udostępnia wiele zintegrowanych w sposób przezroczysty cech,
takich jak:
- proste szablony i odwołania
- zarządzanie pamięcią podręczną
- inteligentne URL-e
- scaffolding
- obsługa wielojęzyczności i międzynarodowości
- rozdzielenie modelu obiektowego i MVC
- obsługa AJAX
- gotowość na zastosowania enterprise

To jest fork autorstwa LExpress oprogramowania symfony 1.

%prep
%setup  -q -n symfony1-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}/%{pkgname}}

cp -a data lib $RPM_BUILD_ROOT%{php_data_dir}/%{pkgname}
ln -s %{php_data_dir}/%{pkgname}/data/bin/%{pkgname} $RPM_BUILD_ROOT%{_bindir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc licenses CHANGELOG.md COPYRIGHT.md LICENSE.md README.md UPGRADE.md WHATS_NEW.md
%attr(755,root,root) %{_bindir}/*
%dir %{php_data_dir}/%{pkgname}
%dir %{php_data_dir}/%{pkgname}/data
%dir %{php_data_dir}/%{pkgname}/data/bin
%attr(755,root,root) %{php_data_dir}/%{pkgname}/data/bin/*
%{php_data_dir}/%{pkgname}/data/[!b]*
%{php_data_dir}/%{pkgname}/lib
