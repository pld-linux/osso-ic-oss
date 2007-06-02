Summary:	Maemo osso library
Summary(pl.UTF-8):	Biblioteka Maemo osso
Name:		osso-ic-oss
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}.tar.gz
# Source0-md5:	6868cbd4dfc78abd7c651428d517e723
Patch0:		%{name}-version.patch
Patch1:		%{name}-dbus.patch
Patch2:		%{name}-noWerror.patch
URL:		http://maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In-place editor library for the Maemo platform.

%description -l pl.UTF-8
Biblioteka edytora dla platformy Maemo.

%package devel
Summary:	Header files for osso-ic-oss
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki osso-ic-oss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/connectivity_preload.sh
%attr(755,root,root) %{_libdir}/libosso-ic.so.*.*.*
%attr(755,root,root) %{_libdir}/libosso-ic-preload.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libosso-ic.so
%{_libdir}/libosso-ic.la
%{_libdir}/libosso-ic-preload.la
%{_includedir}/osso-ic-dbus.h
%{_includedir}/osso-ic-gconf.h
%{_includedir}/osso-ic-ui-dbus.h
%{_includedir}/osso-ic.h
%{_pkgconfigdir}/osso-ic.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso-ic.a
%{_libdir}/libosso-ic-preload.a
