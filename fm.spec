Summary:	Football Manager
Summary(pl):	Menad¿er Pi³karski
Name:		fm
Version:	0.99
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.autismuk.freeserve.co.uk/%{name}-%{version}.tar.gz
# Source0-md5:	9863cf5f9de638748a8fc4bcdb5cddbf
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://freshmeat.net/projects/footballmanager/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Football Manager is a rewrite from scratch of Kevin Toms' famous
Sinclair Spectrum Football Management game. It is not the most
complicated or prettiest game in the world, but it is one of the most
fun.

%description -l pl
Mened¿er Pi³karski jest przepisan± od podstaw s³awn± gr± Sinclair
Spectrum Football Management autorstwa Kevina Tomsa. Nie jest ona
najbardziej skomplikowan± ani najpiêkniejsz± gr± na ¶wiecie, ale jest
jedn± z najbardziej grywalnych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
