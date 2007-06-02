#
Summary:	Maemo osso library
Name:		osso-ic-oss
Version:	1.0.4
Release:	1
License:	LGPL
Group:		Development/Libraries
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

%package devel
Summary:	Header files for osso-ic-oss
Group:		Development/Libraries

%description devel
Header files for osso-ic-oss.

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
%{_libdir}/libosso-ic-preload.so
%attr(755,root,root)    %{_libdir}/libosso-ic.so.0.0.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/osso-ic-dbus.h
%{_includedir}/osso-ic-gconf.h
%{_includedir}/osso-ic-ui-dbus.h
%{_includedir}/osso-ic.h
%{_libdir}/libosso-ic-preload.la
%{_libdir}/libosso-ic.la
%{_libdir}/libosso-ic.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libosso-ic-preload.a
%{_libdir}/libosso-ic.a
%{_pkgconfigdir}/osso-ic.pc
