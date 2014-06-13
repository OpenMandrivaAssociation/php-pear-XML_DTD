%define	_class	XML
%define	_subclass	DTD
%define	modname	%{_class}_%{_subclass}

Summary:	Parsing of DTD files and DTD validation of XML files
Name:		php-pear-%{modname}
Version:	0.5.2
Release:	6
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/XML_DTD/
Source0:	http://download.pear.php.net/package/XML_DTD-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Parsing of DTD files and DTD validation of XML files. The XML
validation is done with the PHP sax parser, the xml extension, it does
not use the domxml extension.

Currently supports most of current XML specification, including
entities, elements and attributes. Some uncommon parts of the
specification may still be unsupported.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/*.txt
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

