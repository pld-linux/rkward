#
# TODO: fix "missing libs" errors 
#
%define		qtver	4.6.2
%define		kdever	4.4.2
Summary:	GUI for the R-project
Summary(pl.UTF-8):	Interfejs dla języka R
Name:		rkward
Version:	0.5.2
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://downloads.sourceforge.net/rkward/%{name}-%{version}.tar.gz
# Source0-md5:	c272660aa2eff52e357c33a8c25e0df5
URL:		http://rkward.sourceforge.net/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	R >= 2.0.0
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	R >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RKWard aims to provide an easily extensible, easy to use GUI for the
R-project, that will one day seamlessly integrate with KOffice. RKWard
tries to combine the power of the R-language with the (relative) ease
of use of commercial tools like SPSS.

%description -l pl.UTF-8
RKWard ma na celu udostępnienie łatwo rozszerzalnego, łatwego w użyciu
środowiska graficzngo dla języka R, które któregoś dnia może zostać
zintegrowane z KOffice. RKWard jest próbą połączenia mocy języka R z
(względną) łatwością użycia komercyjnych narzędzi typu SPSS.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIBR_SO=%{_libdir}/libR.so \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO AUTHORS
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}.bin
%{_desktopdir}/kde4/rkward.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/hicolor/*/apps/rkward.png
%{_iconsdir}/hicolor/*/apps/rkward.svgz
%{_libdir}/R/library/%{name}
