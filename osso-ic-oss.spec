Summary:	Maemo OSSO Internet Connectivity library
Summary(pl.UTF-8):	Biblioteka OSSO Internet Connectivity dla Maemo
Name:		osso-ic-oss
Version:	1.0.4
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}.tar.gz
# Source0-md5:	6868cbd4dfc78abd7c651428d517e723
Patch0:		%{name}-version.patch
Patch1:		%{name}-dbus.patch
Patch2:		%{name}-noWerror.patch
URL:		http://maemo.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	intltool
BuildRequires:	libosso-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSO Internet Connectivity library for Maemo platform.

%description -l pl.UTF-8
Biblioteka OSSO Internet Connectivity (łączności z Internetem) dla
platformy Maemo.

%package devel
Summary:	Header files for osso-ic-oss
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki osso-ic-oss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GConf2-devel >= 2.0
Requires:	dbus-devel >= 0.60
Requires:	libosso-devel

%description devel
Header files for osso-ic-oss.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki osso-ic-oss.

%package static
Summary:	Static osso-ic-oss library
Summary(pl.UTF-8):	Statyczna biblioteka osso-ic-oss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboss library.

%description static -l pl.UTF-8
Statyczna biblioteka osso-ic-oss.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libosso-ic-preload.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libosso-ic.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/connectivity_preload.sh
%attr(755,root,root) %{_libdir}/libosso-ic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosso-ic.so.0
%attr(755,root,root) %{_libdir}/libosso-ic-preload.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libosso-ic.so
%{_includedir}/osso-ic-dbus.h
%{_includedir}/osso-ic-gconf.h
%{_includedir}/osso-ic-ui-dbus.h
%{_includedir}/osso-ic.h
%{_pkgconfigdir}/osso-ic.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso-ic.a
