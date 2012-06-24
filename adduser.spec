Summary:     Script for easy adding users
Summary(pl): Skrypt do prostego dodawania u�ytkownik�w
Name:        adduser
Version:     1.06
Release:     2
Copyright:   GPL
Source:      %{name}-%{version}.tar.gz
Group:       Utilities/System
Group(pl):   Narz�dzia/System
Requires:    shadow
Obsoletes:   etcskel
Provides:    etcskel
BuildArch:   noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Interactive shell script for easy adding new users to the system.
Package contains files copied to new users home directories.

%description -l pl
Skrypt shella pozwalaj�cy interaktywnie dodawa� nowych u�ytkownik�w
do systemu. Pakiet zawiera pliki kopiowane do katalog�w domowych
nowych u�ytkownik�w.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{sbin,share/locale/pl/LC_MESSAGES} \
	$RPM_BUILD_ROOT/etc/{skel,adduser.d,default/public_html/{pl,en}}

install adduser $RPM_BUILD_ROOT%{_sbindir}
install adduser.conf $RPM_BUILD_ROOT/etc/default/adduser

cp -R etcskel/. $RPM_BUILD_ROOT/etc/skel

for lang in pl en; do
  cp -R etcskel/$lang/public_html/* $RPM_BUILD_ROOT/etc/default/public_html/$lang
  rm -rf $RPM_BUILD_ROOT/etc/skel/$lang/public_html
done
ln -sf en $RPM_BUILD_ROOT/etc/skel/default
msgfmt po/pl.po -o $RPM_BUILD_ROOT%{_datadir}/locale/pl/LC_MESSAGES/adduser.mo

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(700,root,root) %{_sbindir}/*

%attr(750,root,root) %dir /etc/adduser.d
%attr(700,root,root) %dir /etc/skel/C
%attr(700,root,root) %dir %lang(pl) /etc/skel/pl
%attr(700,root,root) %dir %lang(en) /etc/skel/en

%attr(640,root,root) %config %verify(not size mtime md5) /etc/default/adduser
%attr(600,root,root) %config %verify(not size mtime md5) /etc/skel/C/*
%attr(600,root,root) %config %verify(not size mtime md5) %lang(pl) /etc/skel/pl/*
%attr(600,root,root) %config %verify(not size mtime md5) %lang(en) /etc/skel/en/*
%verify(not link) /etc/skel/default

%dir /etc/default/public_html
%config %verify(not size mtime md5) /etc/default/public_html/*
