%define major 5
%define libname %mklibname KF5Ldap %{major}
%define devname %mklibname KF5Ldap -d

Name: kldap
Version:	23.08.5
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	2
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for accessing LDAP directories
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(ldap)
BuildRequires: sasl-devel
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KPim5Mbox)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Keychain)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: akonadi-contacts
Conflicts: kio-ldap < 3:16.04.3-2
Obsoletes: kio-ldap < 3:16.04.3-2
Provides: kio-ldap = 3:16.04.3-2

%description
KDE library for accessing LDAP directories.

%package -n %{libname}
Summary: KDE library for accessing LDAP directories
Group: System/Libraries

%description -n %{libname}
KDE library for accessing LDAP directories.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/kldap.categories
%{_datadir}/qlogging-categories5/kldap.renamecategories
%{_libdir}/qt5/plugins/kf5/kio/ldap.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{qch,tags}
