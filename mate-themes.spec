%define mate_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Themes for MATE
Name:		mate-themes
Version:	3.22.24
Release:	2
License:	LGPLv2+ and GPLv2+ and GPLv3+
Group:		Graphical desktop/Other
Url:		https://mate-desktop.org
Source0:	https://pub.mate-desktop.org/releases/themes/%{mate_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	autoconf-archive
BuildRequires:	intltool
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk-engines-2)

Requires:	gtk-engines2
Requires:	mate-icon-theme
Requires:	murrine

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This packages provides Themes for MATE.

%files
%doc AUTHORS COPYING README
%dir %{_iconsdir}/ContrastHigh/
%{_iconsdir}/ContrastHigh/*/
%{_iconsdir}/ContrastHigh/index.theme
%ghost %{_iconsdir}/ContrastHigh/icon-theme.cache
%dir %{_iconsdir}/mate-black/
%{_iconsdir}/mate-black/*/
%{_iconsdir}/mate-black/index.theme
%{_iconsdir}/mate/
%{_datadir}/themes/*

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=yes ./autogen.sh
%configure
%make_build

%install
%make_install
touch %{buildroot}%{_iconsdir}/ContrastHigh/icon-theme.cache

%post
%update_icon_cache ContrastHigh

%postun
%clean_icon_cache ContrastHigh

