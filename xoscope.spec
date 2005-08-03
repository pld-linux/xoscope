# TODO
# - doesn't build on amd64:
# gr_gtk.c: In function `setbits':
# gr_gtk.c:524: warning: cast from pointer to integer of different size
Summary:	xoscope - digital oscilloscope on PC
Summary(pl):	xoscope - cyfrowy oscyloskop na PC
Name:		xoscope
Version:	1.12
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xoscope/%{name}-%{version}.tgz
# Source0-md5:	89f8019a772713a976b634305d29cfe5
Patch0:		xoscope-pmake.patch
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
x*oscope jest to cyfrowy oscyloskop, kt�ry u�ywa jako sygna�u
wej�ciowego karty d�wi�kowej (/dev/dsp albo EsounD) i/lub Radio Shack
ProbeScope znanego tak�e jako osziFOX.

%prep
%setup -q
%patch0 -p1

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
%{_libdir}/%{name}
%{_mandir}/*/*
