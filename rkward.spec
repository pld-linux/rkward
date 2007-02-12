Summary:	GUI for the R-project
Summary(pl.UTF-8):   Interfejs dla R
Name:		rkward
Version:	0.3.4
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/rkward/%{name}-%{version}.tar.gz
# Source0-md5:	87b20698228bdb211b17fcb3385ec93a
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

%description -l pl.UTF-8
RKWard chce udostępniać łatwo rozszerzalne, łatwe w użyciu środowisko
graficzne dla R, które któregoś dnia zostanie zintegrowane z KOffice.
RKWard stara się połączyć moc języka R z (względną) łatwością użycia
komercyjnych narzędzi typu SPSS.

%prep
%setup -q

%build
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
cp -f /usr/share/automake/config.sub admin
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
R CMD INSTALL %{name} --library=$RPM_BUILD_ROOT%{_libdir}/R/library
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
%{_iconsdir}/crystalsvg/*/*/*.png
%{_libdir}/R/library/%{name}
