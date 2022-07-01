Name: openclipart
Version: 0.16
Release: 1ark
Summary: A clip art collection
URL: http://www.openclipart.org/
Source: %name-%version.tar.bz2
License: Public Domain
Group: Applications/Publishing
Prefix: %_datadir/%name
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

%description
A clip art collection.

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_datadir/%name
cp -a * $RPM_BUILD_ROOT%_datadir/%name

%files
%defattr(-,root,root)
%_datadir/%name

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}

%changelog
* Mon Jul 18 2005 Jonadab the Unsightly One
- Updated to version number 0.16

* Mon Jul 11 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.15-1ark
- 0.15

* Sat May 14 2005 Bernhard Rosenkraenzer <bero@arklinux.org> 0.13.2-1ark
- initial RPM
