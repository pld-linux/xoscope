# TODO: broken on archs with sizeof(int)!=sizeof(void*) (i.e. all 64-bit)
#       (it abuses guint field to place strings - see gr_gtk.c:670 and below)
Summary:	xoscope - digital oscilloscope on PC
Summary(pl.UTF-8):	xoscope - cyfrowy oscyloskop na PC
Name:		xoscope
Version:	2.0
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xoscope/%{name}-%{version}.tgz
# Source0-md5:	f1430ccee4ee0f6f478c2cd209549741
Patch0:		xoscope-2.0-3.1-nmu.diff
URL:		http://xoscope.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gtk+2-devel >= 2.2
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x*oscope is a digital oscilloscope that uses a sound card (via
/dev/dsp or EsounD) and/or Radio Shack ProbeScope a.k.a osziFOX as the
signal input.

%description -l pl.UTF-8
x*oscope jest to cyfrowy oscyloskop, który używa jako sygnału
wejściowego karty dźwiękowej (/dev/dsp albo EsounD) i/lub Radio Shack
ProbeScope znanego także jako osziFOX.

%prep
%setup -q
%patch -p1

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
%doc AUTHORS ChangeLog hardware/HARDWARE NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
