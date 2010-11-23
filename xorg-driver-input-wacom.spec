Summary:	X.org input driver for Wacom tablets
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla tabletów Wacom
Name:		xorg-driver-input-wacom
Version:	0.10.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/linuxwacom/xf86-input-wacom/xf86-input-wacom-%{version}.tar.bz2
# Source0-md5:	4070b27443758310dbcbf84158c8eeb1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autogen
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-xserver-server-devel
%requires_xorg_xserver_xinput
Obsoletes:	linuxwacom
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Wacom tablets.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla tabletów Wacom

%package devel
Summary:	Header file for wacom driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika wacom
Group:		Development/Libraries

%description devel
Header file for wacom driver

%description devel -l pl.UTF-8
Plik nagłówkowy sterownika wacom

%prep
%setup -q -n xf86-input-wacom-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--enable-static \
	--enable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/xorg/modules/input/wacom_drv.*
%attr(755,root,root) %{_bindir}/xsetwacom
%{_datadir}/X11/xorg.conf.d/50-wacom.conf
%{_mandir}/man1/xsetwacom.1*
%{_mandir}/man4/wacom.4*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isdv4-serial-debugger
%{_includedir}/xorg/Xwacom.h
%{_includedir}/xorg/wacom-properties.h
%{_includedir}/xorg/isdv4.h
%{_pkgconfigdir}/xorg-wacom.pc
