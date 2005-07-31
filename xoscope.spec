Summary:	xoscope - digital oscilloscope on pc
Summary(pl):	xoscope - cyfrowy oscyloskop na pc
Name:		xoscope
Version:	1.12
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xoscope/%{name}-%{version}.tgz
# Source0-md5:	89f8019a772713a976b634305d29cfe5
URL:		http://xoscope.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
Buildrequires:	perl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x*oscope is a digital oscilloscope that uses a sound card (via
/dev/dsp or EsounD) and/or Radio Shack ProbeScope a.k.a osziFOX as the
signal input.

%description -l pl
x*oscope jest to cyfrowy oscyloskop który u¿ywa karty d¼wiêkowej
(/dev/dsp albo EsounD) i/albo Radio Shack ProbeScope znany tak¿e jako
osziFOX jako sygna³ wej¶ciowy.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HARDWARE INTERNALS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%{_libdir}/%{name}
