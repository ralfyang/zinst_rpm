Name: zinst
Version:	4.1.4
Release:	1%{?dist}
Summary:	Package oriented management system

Group:		RalfYang
License:	LGPL v2.0
URL:		http://ralfyang.com
Source0:	zinst-4.1.4.tgz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	/bin/bash
Requires:	wget, bc, bash, sudo, tar, openssh-clients

%description
https://github.com/goody80/Ralf_Dev
For the centralized package manager & distributed systems

%prep
%setup -q

%build
#configure
#make %{?_smp_mflags}

%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/zinst_starters/
cp * $RPM_BUILD_ROOT/usr/local/zinst_starters/


%files
%defattr(-,root,wheel,-)
/usr/local/*
%doc

%post
cp /usr/local/zinst_starters/zinst /usr/bin/zinst

%clean
rm -rf %{buildroot} /usr/local/zinst_starters/


%changelog

