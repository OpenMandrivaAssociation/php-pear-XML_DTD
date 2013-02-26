%define		_class		XML
%define		_subclass	DTD
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.5.1
Release:	%mkrel 7
Summary:	Parsing of DTD files and DTD validation of XML files
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_DTD/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Parsing of DTD files and DTD validation of XML files. The XML
validation is done with the PHP sax parser, the xml extension, it does
not use the domxml extension.

Currently supports most of current XML specification, including
entities, elements and attributes. Some uncommon parts of the
specification may still be unsupported.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/*.txt
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-5mdv2011.0
+ Revision: 667661
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-4mdv2011.0
+ Revision: 607167
- rebuild

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-3mdv2010.1
+ Revision: 464948
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 441667
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.5.1-1mdv2009.1
+ Revision: 368293
- Update php pear XML_DTD to 0.5.1 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-9mdv2009.1
+ Revision: 322774
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-8mdv2009.0
+ Revision: 237159
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-7mdv2007.0
+ Revision: 82845
- Import php-pear-XML_DTD

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-1mdk
- initial Mandriva package (PLD import)

