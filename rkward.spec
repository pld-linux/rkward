Summary:	GUI for the R-project
Summary(pl):	Interfejs dla R
Name:		rkward
Version:	0.3.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/rkward/%{name}-%{version}.tar.gz
# Source0-md5:	54323e767dc33191fb43cabdc9b01118
URL:		http://rkward.sourceforge.net/
BuildRequires:	R-base >= 2.0.0
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	R-base >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RKWard aims to provide an easily extensible, easy to use GUI for the
R-project, that will one day seamlessly integrate with KOffice. RKWard
tries to combine the power of the R-language with the (relative) ease
of use of commercial tools like SPSS.

%description -l pl
RKWard chce udostêpniaæ ³atwo rozszerzalne, ³atwe w u¿yciu ¶rodowisko
graficzne dla R, które którego¶ dnia zostanie zintegrowane z KOffice.
RKWard stara siê po³±czyæ moc jêzyka R z (wzglêdn±) ³atwo¶ci± u¿ycia
komercyjnych narzêdzi typu SPSS.

%prep
%setup -q -n %{name}

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_libdir}/R/library}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install rkward/rkward.desktop $RPM_BUILD_ROOT%{_desktopdir}
cd rkward/rbackend/rpackages
R CMD INSTALL %{name} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/
cd -

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --htmllist)
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/*/*/*/*.png
%{_libdir}/R/library/%{name}
