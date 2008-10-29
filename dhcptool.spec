Summary:	Generates and transmits custom DHCP/BOOTP packets
Name:		dhcptool
Version:	0.9b
Release:	%mkrel 2
License:	BSD
Group:		Networking/Other
URL:		http://www.gatorhole.se/index.php?product=dhcp&lang=gb
Source0:	http://www.gatorhole.com/downloads/%{name}-%{version}.tar.gz
Patch0:		dhcptool-0.9b-DESTDIR.diff
BuildRequires:	pcap-devel
BuildRequires:	net-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
DHCPTool is a command-line utility used to e.g. test DHCP servers or DHCP relay
agents. It can generate almost any kind of DHCP packet, and the idea is to
facilitate simulation of e.g. broken DHCP clients to see how well servers
handle them and/or to detect stability bugs in any software that parses DHCP
messages.

%prep

%setup -q
%patch0 -p0

%build
rm -f configure
autoreconf -fis

%configure2_5x

%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE
%{_bindir}/*
%{_mandir}/*/*

