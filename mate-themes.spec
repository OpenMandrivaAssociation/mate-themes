%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Themes for MATE
Name:		mate-themes
Version:	3.20.9
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	intltool
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk-engines-2)
Requires:	gtk-engines2
Requires:	mate-icon-theme
Requires:	murrine

%description
This packages contains Themes for MATE.

%files
%doc README NEWS AUTHORS
%{_datadir}/themes/BlackMATE/
%{_datadir}/themes/BlueMenta/
%{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/ContrastHighInverse/
%{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/HighContrast/
%{_datadir}/themes/Menta/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/Shiny/
%{_iconsdir}/ContrastHigh/
%{_iconsdir}/mate/

#---------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
