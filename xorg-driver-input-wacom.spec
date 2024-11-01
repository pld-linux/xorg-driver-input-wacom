Summary:	X.org input driver for Wacom tablets
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla tabletów Wacom
Name:		xorg-driver-input-wacom
Version:	1.2.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxwacom/xf86-input-wacom/releases
Source0:	https://github.com/linuxwacom/xf86-input-wacom/releases/download/xf86-input-wacom-%{version}/xf86-input-wacom-%{version}.tar.bz2
# Source0-md5:	ef8a6cc34623db6c3482508374863d51
URL:		https://linuxwacom.github.io/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	doxygen >= 1.6.1
BuildRequires:	pkgconfig
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.13.0
Requires:	xorg-xserver-server >= 1.13.0
%requires_xorg_xserver_xinput
Obsoletes:	linuxwacom < 0.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Wacom tablets.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla tabletów Wacom.

%package devel
Summary:	Header file for wacom driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika wacom
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Header file for wacom driver.

%description devel -l pl.UTF-8
Plik nagłówkowy sterownika wacom.

%prep
%setup -q -n xf86-input-wacom-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-debug \
	--with-systemd-unit-dir=%{systemdunitdir} \
	--with-udev-rules-dir=/lib/udev/rules.d

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/input/wacom_drv.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/isdv4-serial-inputattach
%attr(755,root,root) %{_bindir}/xsetwacom
%attr(755,root,root) %{_libdir}/xorg/modules/input/wacom_drv.so
%{_datadir}/X11/xorg.conf.d/70-wacom.conf
%{systemdunitdir}/wacom-inputattach@.service
/lib/udev/rules.d/wacom.rules
%{_mandir}/man1/xsetwacom.1*
%{_mandir}/man4/wacom.4*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isdv4-serial-debugger
%{_includedir}/xorg/Xwacom.h
%{_includedir}/xorg/wacom-properties.h
%{_includedir}/xorg/wacom-util.h
%{_includedir}/xorg/isdv4.h
%{_pkgconfigdir}/xorg-wacom.pc
