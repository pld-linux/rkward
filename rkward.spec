Summary:	GUI for the R-project
Summary(pl):	Interfejs dla R
Name:		rkward
Version:	0.2.8
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	aa874192895ca0d83fc0311599c87c98
URL:		http://rkward.sourceforge.net/
BuildRequires:	R-base
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RKWard aims to provide an easily extensible, easy to use GUI for the
R-project, that will one day seamlessly integrate with KOffice. RKWard
tries to combine the power of the R-language with the (relative) ease
of use of commercial tools like SPSS.

%description -l pl
RKWard chce udost�pnia� �atwo rozszerzalne, �atwe w u�yciu �rodowisko
graficzne dla R, kt�re kt�rego� dnia zostanie zintegrowane z KOffice.
RKWard stara si� po��czy� moc j�zyka R z (wzgl�dn�) �atwo�ci� u�ycia
komercyjnych narz�dzi typu SPSS.

%prep
%setup -q

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
cp -f %{_datadir}/automake/config.sub admin
CXXFLAGS="%{rpmcflags} -I%{_includedir}/R"
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# %find_lang %{name} --with-kde
install rkward/rkward.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
%{_datadir}/apps/katepart/syntax/r.xml
%{_iconsdir}/*/*/*/*.png
%lang(en) %{_kdedocdir}/en/%{name}
